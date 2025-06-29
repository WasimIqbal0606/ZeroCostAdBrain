"""
Live data integration module for the multi-agent advertising brain app.
Fetches real-time data from free APIs to enhance trend analysis and insights.
"""

import requests
import json
import logging
from typing import Dict, List, Any, Optional
from datetime import datetime, timedelta
import os

logger = logging.getLogger(__name__)

class LiveDataFetcher:
    """Fetches live data from various free APIs."""
    
    def __init__(self):
        self.base_timeout = 10
        
    def get_reddit_trends(self, subreddit: str = "all", limit: int = 10) -> List[Dict]:
        """Fetch trending posts from Reddit."""
        try:
            url = f"https://www.reddit.com/r/{subreddit}/hot.json"
            headers = {'User-Agent': 'AdvertisingBrainApp/1.0'}
            
            response = requests.get(url, headers=headers, timeout=self.base_timeout)
            
            if response.status_code == 200:
                data = response.json()
                posts = data.get('data', {}).get('children', [])
                
                trends = []
                for post in posts[:limit]:
                    post_data = post.get('data', {})
                    trends.append({
                        'title': post_data.get('title', ''),
                        'score': post_data.get('score', 0),
                        'comments': post_data.get('num_comments', 0),
                        'subreddit': post_data.get('subreddit', ''),
                        'created': datetime.fromtimestamp(post_data.get('created_utc', 0)).isoformat(),
                        'url': f"https://reddit.com{post_data.get('permalink', '')}"
                    })
                
                return trends
            
        except Exception as e:
            logger.error(f"Error fetching Reddit trends: {e}")
        
        return []
    
    def get_news_headlines(self, category: str = "business") -> List[Dict]:
        """Fetch latest news headlines from NewsAPI."""
        try:
            # Using NewsAPI free tier (requires API key)
            api_key = os.getenv("NEWS_API_KEY")
            if not api_key:
                # Fallback to free news source
                return self._get_free_news()
            
            url = "https://newsapi.org/v2/top-headlines"
            params = {
                'apiKey': api_key,
                'category': category,
                'country': 'us',
                'pageSize': 10
            }
            
            response = requests.get(url, params=params, timeout=self.base_timeout)
            
            if response.status_code == 200:
                data = response.json()
                articles = data.get('articles', [])
                
                news = []
                for article in articles:
                    news.append({
                        'title': article.get('title', ''),
                        'description': article.get('description', ''),
                        'source': article.get('source', {}).get('name', ''),
                        'published': article.get('publishedAt', ''),
                        'url': article.get('url', '')
                    })
                
                return news
            
        except Exception as e:
            logger.error(f"Error fetching news: {e}")
        
        return self._get_free_news()
    
    def _get_free_news(self) -> List[Dict]:
        """Fallback free news source."""
        try:
            # Using JSONPlaceholder for demo data
            url = "https://jsonplaceholder.typicode.com/posts"
            response = requests.get(url, timeout=self.base_timeout)
            
            if response.status_code == 200:
                posts = response.json()[:5]  # Get first 5 posts
                
                news = []
                for post in posts:
                    news.append({
                        'title': post.get('title', '').title(),
                        'description': post.get('body', '')[:100] + '...',
                        'source': 'Sample News',
                        'published': datetime.now().isoformat(),
                        'url': f"https://example.com/news/{post.get('id', '')}"
                    })
                
                return news
                
        except Exception as e:
            logger.error(f"Error fetching fallback news: {e}")
        
        return []
    
    def get_github_trending(self, language: str = "", since: str = "daily") -> List[Dict]:
        """Fetch trending GitHub repositories."""
        try:
            url = "https://api.github.com/search/repositories"
            
            # Build query for trending repos
            date_threshold = datetime.now() - timedelta(days=1 if since == "daily" else 7)
            date_str = date_threshold.strftime("%Y-%m-%d")
            
            query = f"created:>{date_str}"
            if language:
                query += f" language:{language}"
            
            params = {
                'q': query,
                'sort': 'stars',
                'order': 'desc',
                'per_page': 10
            }
            
            response = requests.get(url, params=params, timeout=self.base_timeout)
            
            if response.status_code == 200:
                data = response.json()
                repos = data.get('items', [])
                
                trending = []
                for repo in repos:
                    trending.append({
                        'name': repo.get('full_name', ''),
                        'description': repo.get('description', ''),
                        'stars': repo.get('stargazers_count', 0),
                        'language': repo.get('language', ''),
                        'created': repo.get('created_at', ''),
                        'url': repo.get('html_url', '')
                    })
                
                return trending
            
        except Exception as e:
            logger.error(f"Error fetching GitHub trends: {e}")
        
        return []
    
    def get_crypto_trends(self) -> List[Dict]:
        """Fetch cryptocurrency trending data."""
        try:
            # Using CoinGecko free API
            url = "https://api.coingecko.com/api/v3/search/trending"
            
            response = requests.get(url, timeout=self.base_timeout)
            
            if response.status_code == 200:
                data = response.json()
                coins = data.get('coins', [])
                
                trends = []
                for coin in coins:
                    coin_data = coin.get('item', {})
                    trends.append({
                        'name': coin_data.get('name', ''),
                        'symbol': coin_data.get('symbol', ''),
                        'rank': coin_data.get('market_cap_rank', 0),
                        'price_btc': coin_data.get('price_btc', 0),
                        'thumb': coin_data.get('thumb', ''),
                        'url': f"https://www.coingecko.com/en/coins/{coin_data.get('id', '')}"
                    })
                
                return trends
            
        except Exception as e:
            logger.error(f"Error fetching crypto trends: {e}")
        
        return []
    
    def get_weather_data(self, city: str = "New York") -> Dict:
        """Fetch current weather data."""
        try:
            # Using OpenWeatherMap free API
            api_key = os.getenv("OPENWEATHER_API_KEY")
            if not api_key:
                return self._get_mock_weather(city)
            
            url = "http://api.openweathermap.org/data/2.5/weather"
            params = {
                'q': city,
                'appid': api_key,
                'units': 'metric'
            }
            
            response = requests.get(url, params=params, timeout=self.base_timeout)
            
            if response.status_code == 200:
                data = response.json()
                
                return {
                    'city': data.get('name', ''),
                    'country': data.get('sys', {}).get('country', ''),
                    'temperature': data.get('main', {}).get('temp', 0),
                    'description': data.get('weather', [{}])[0].get('description', ''),
                    'humidity': data.get('main', {}).get('humidity', 0),
                    'wind_speed': data.get('wind', {}).get('speed', 0)
                }
            
        except Exception as e:
            logger.error(f"Error fetching weather: {e}")
        
        return self._get_mock_weather(city)
    
    def _get_mock_weather(self, city: str) -> Dict:
        """Fallback weather data."""
        return {
            'city': city,
            'country': 'US',
            'temperature': 22,
            'description': 'partly cloudy',
            'humidity': 65,
            'wind_speed': 3.5
        }
    
    def get_comprehensive_trends(self, topic: str) -> Dict[str, Any]:
        """Fetch comprehensive trending data related to a topic."""
        trends_data = {
            'topic': topic,
            'timestamp': datetime.now().isoformat(),
            'sources': {}
        }
        
        # Fetch from multiple sources
        trends_data['sources']['reddit'] = self.get_reddit_trends(limit=5)
        trends_data['sources']['news'] = self.get_news_headlines()
        trends_data['sources']['github'] = self.get_github_trending()
        trends_data['sources']['crypto'] = self.get_crypto_trends()
        trends_data['sources']['weather'] = self.get_weather_data()
        
        return trends_data
    
    def analyze_trend_signals(self, trends_data: Dict) -> Dict[str, Any]:
        """Analyze trend signals from collected data."""
        signals = {
            'social_momentum': 0,
            'news_relevance': 0,
            'tech_innovation': 0,
            'market_interest': 0,
            'overall_score': 0
        }
        
        try:
            # Analyze Reddit engagement
            reddit_posts = trends_data.get('sources', {}).get('reddit', [])
            if reddit_posts:
                avg_score = sum(post.get('score', 0) for post in reddit_posts) / len(reddit_posts)
                signals['social_momentum'] = min(int(avg_score / 100), 10)  # Normalize to 0-10
            
            # Analyze news coverage
            news_articles = trends_data.get('sources', {}).get('news', [])
            signals['news_relevance'] = min(len(news_articles), 10)
            
            # Analyze GitHub activity
            github_repos = trends_data.get('sources', {}).get('github', [])
            if github_repos:
                avg_stars = sum(repo.get('stars', 0) for repo in github_repos) / len(github_repos)
                signals['tech_innovation'] = min(int(avg_stars / 100), 10)
            
            # Analyze crypto trends
            crypto_trends = trends_data.get('sources', {}).get('crypto', [])
            signals['market_interest'] = min(len(crypto_trends), 10)
            
            # Calculate overall score
            signals['overall_score'] = int(sum(signals.values()) / 4)
            
        except Exception as e:
            logger.error(f"Error analyzing trend signals: {e}")
        
        return signals