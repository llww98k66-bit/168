import time
from abc import ABC, abstractmethod
from typing import List, Dict, Any
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from src.utils.logger import setup_logger


logger = setup_logger(__name__)


class BaseCrawler(ABC):
    """Base crawler class with common functionality."""
    
    def __init__(self, timeout: int = 30, retry_count: int = 3):
        self.timeout = timeout
        self.retry_count = retry_count
        self.session = self._create_session()
    
    def _create_session(self) -> requests.Session:
        """Create a requests session with retry strategy."""
        session = requests.Session()
        
        retry_strategy = Retry(
            total=self.retry_count,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504],
        )
        
        adapter = HTTPAdapter(max_retries=retry_strategy)
        session.mount("http://", adapter)
        session.mount("https://", adapter)
        
        return session
    
    def _set_headers(self) -> Dict[str, str]:
        """Set request headers."""
        return {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
    
    def get(self, url: str) -> str:
        """Fetch content from URL."""
        try:
            response = self.session.get(
                url,
                headers=self._set_headers(),
                timeout=self.timeout
            )
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            logger.error(f"Error fetching {url}: {e}")
            raise
    
    def post(self, url: str, data: Dict[str, Any]) -> str:
        """Post data to URL."""
        try:
            response = self.session.post(
                url,
                json=data,
                headers=self._set_headers(),
                timeout=self.timeout
            )
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            logger.error(f"Error posting to {url}: {e}")
            raise
    
    @abstractmethod
    def crawl(self) -> List[Dict[str, Any]]:
        """Crawl data from source. Must be implemented by subclasses."""
        pass
    
    def close(self):
        """Close the session."""
        self.session.close()
