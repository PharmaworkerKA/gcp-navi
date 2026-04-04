"""GCP実務ナビ - ブログ固有設定"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent

BLOG_NAME = "GCP実務ナビ"
BLOG_DESCRIPTION = (
    "臨床試験のGCP（Good Clinical Practice）実務知識を毎日更新。"
    "海外の最新ICH-GCPガイドライン動向を日本語で翻訳・要約し、"
    "CRA・CRC向けに実践的に解説。"
)
BLOG_URL = "https://pharmaworkerka.github.io/gcp-navi"
BLOG_TAGLINE = "GCP実務の最新情報を日本語で発信"
BLOG_LANGUAGE = "ja"

GITHUB_REPO = "PharmaworkerKA/gcp-navi"
GITHUB_BRANCH = "gh-pages"
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")

OUTPUT_DIR = BASE_DIR / "output"
ARTICLES_DIR = OUTPUT_DIR / "articles"
SITE_DIR = OUTPUT_DIR / "site"
TOPICS_DIR = OUTPUT_DIR / "topics"

TARGET_CATEGORIES = [
    "ICH-GCPガイドライン",
    "モニタリング実務",
    "同意説明文書・ICF",
    "査察対応",
    "GCP最新ニュース",
    "リスクベースドモニタリング",
    "治験届・申請実務",
    "海外トレンド翻訳",
]

THEME = {
    "primary": "#059669",
    "accent": "#064e3b",
    "gradient_start": "#059669",
    "gradient_end": "#047857",
    "dark_bg": "#0f172a",
    "dark_surface": "#1e293b",
    "light_bg": "#f0fdf4",
    "light_surface": "#ffffff",
}

MAX_ARTICLE_LENGTH = 4000
ARTICLES_PER_DAY = 1
SCHEDULE_HOURS = [8]

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
GEMINI_MODEL = "gemini-2.5-flash-lite"

ENABLE_SEO_OPTIMIZATION = True
MIN_SEO_SCORE = 75
MIN_KEYWORD_DENSITY = 1.0
MAX_KEYWORD_DENSITY = 3.0
META_DESCRIPTION_LENGTH = 120
ENABLE_INTERNAL_LINKS = True

AFFILIATE_LINKS = {
    "SAS認定資格": {
        "url": "https://www.sas.com/ja_jp/certification.html",
        "text": "SAS認定資格を取得する",
        "description": "SASプログラミングの公式認定",
    },
    "Amazon GCP書籍": {
        "url": "https://www.amazon.co.jp",
        "text": "AmazonでGCP関連書籍を探す",
        "description": "GCP・臨床試験の参考書",
    },
    "Udemy 臨床開発講座": {
        "url": "https://www.udemy.com",
        "text": "Udemyで臨床開発講座を探す",
        "description": "動画で学ぶGCP・臨床開発",
    },
    "楽天 医療書籍": {
        "url": "https://www.rakuten.co.jp",
        "text": "楽天で医療書籍を探す",
        "description": "製薬・臨床開発の参考書",
    },
}
AFFILIATE_TAG = "musclelove07-22"

ADSENSE_CLIENT_ID = os.environ.get("ADSENSE_CLIENT_ID", "")
ADSENSE_ENABLED = bool(ADSENSE_CLIENT_ID)

DASHBOARD_HOST = "127.0.0.1"
DASHBOARD_PORT = 8091

# Google Analytics (GA4)
GOOGLE_ANALYTICS_ID = "G-CSFVD34MKK"

# Google Search Console 認証ファイル
SITE_VERIFICATION_FILES = {
    "googlea31edabcec879415.html": "google-site-verification: googlea31edabcec879415.html",
}

# コンテンツ画像設定（Google Drive から記事内に画像を自動挿入）
CONTENT_IMAGES_ENABLED = True
CONTENT_IMAGES_FOLDER_ID = os.environ.get("CONTENT_IMAGES_FOLDER_ID", "")
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY", "")
CONTENT_IMAGES_PER_ARTICLE = 3
