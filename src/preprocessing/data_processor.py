import pandas as pd
import numpy as np
from pathlib import Path
from typing import Tuple, List
from src.utils.logger import setup_logger


logger = setup_logger(__name__)


class DataProcessor:
    """Process and prepare lottery data for model training."""
    
    def __init__(self, raw_path: str = "data/raw", processed_path: str = "data/processed"):
        self.raw_path = Path(raw_path)
        self.processed_path = Path(processed_path)
        self.processed_path.mkdir(parents=True, exist_ok=True)
    
    def load_raw_data(self, filename: str) -> pd.DataFrame:
        """Load raw data from CSV or JSON."""
        file_path = self.raw_path / filename
        
        if not file_path.exists():
            logger.warning(f"File not found: {file_path}")
            return pd.DataFrame()
        
        try:
            if filename.endswith('.csv'):
                df = pd.read_csv(file_path)
            elif filename.endswith('.json'):
                df = pd.read_json(file_path)
            else:
                raise ValueError(f"Unsupported file format: {filename}")
            
            logger.info(f"Loaded {len(df)} rows from {filename}")
            return df
        except Exception as e:
            logger.error(f"Error loading data: {e}")
            return pd.DataFrame()
    
    def clean_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """Clean and preprocess data."""
        # Remove duplicates
        df = df.drop_duplicates()
        
        # Remove rows with missing values
        df = df.dropna()
        
        # Sort by date
        if 'date' in df.columns:
            df['date'] = pd.to_datetime(df['date'])
            df = df.sort_values('date')
        
        logger.info(f"Cleaned data: {len(df)} rows remaining")
        return df
    
    def extract_features(self, df: pd.DataFrame) -> Tuple[np.ndarray, np.ndarray]:
        """Extract features from lottery data."""
        if df.empty:
            return np.array([]), np.array([])
        
        # Extract numbers
        if 'numbers' in df.columns:
            numbers = df['numbers'].tolist()
            # Convert to feature vectors
            X = np.array([self._numbers_to_features(nums) for nums in numbers])
        else:
            X = np.array([])
        
        # Extract target (future numbers)
        if len(X) > 1:
            y = X[1:]
            X = X[:-1]
        else:
            y = np.array([])
        
        logger.info(f"Extracted {len(X)} feature vectors")
        return X, y
    
    def _numbers_to_features(self, numbers: List[int]) -> np.ndarray:
        """Convert number sequence to feature vector."""
        # One-hot encoding or frequency encoding
        features = np.zeros(10)  # For digits 0-9
        for num in numbers:
            if 0 <= num <= 9:
                features[num] += 1
        return features
    
    def save_processed_data(self, X: np.ndarray, y: np.ndarray, name: str):
        """Save processed data to file."""
        np.save(self.processed_path / f"{name}_X.npy", X)
        np.save(self.processed_path / f"{name}_y.npy", y)
        logger.info(f"Saved processed data: {name}")
    
    def load_processed_data(self, name: str) -> Tuple[np.ndarray, np.ndarray]:
        """Load processed data from file."""
        try:
            X = np.load(self.processed_path / f"{name}_X.npy")
            y = np.load(self.processed_path / f"{name}_y.npy")
            logger.info(f"Loaded processed data: {name}")
            return X, y
        except FileNotFoundError:
            logger.warning(f"Processed data not found: {name}")
            return np.array([]), np.array([])
