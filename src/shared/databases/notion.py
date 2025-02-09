import os
from typing import List, Dict
from dotenv import load_dotenv
from notion_client import AsyncClient, APIResponseError

# Load environment variables first
load_dotenv()

NOTION_API_TOKEN = os.getenv("NOTION_API_TOKEN")
NOTION_FEEDS_DATABASE_ID = os.getenv("NOTION_FEEDS_DATABASE_ID")
CI = os.getenv("CI")

# Initialize Notion client with proper logging
notion = AsyncClient(
    auth=NOTION_API_TOKEN,
    log_level="INFO" if CI else "DEBUG"
)

async def get_feed_urls_from_notion() -> List[Dict[str, str]]:
    """
    Retrieves enabled feed URLs from Notion database
    Returns list of dictionaries with 'url' and 'title' keys
    """
    try:
        response = await notion.databases.query(
            database_id=NOTION_FEEDS_DATABASE_ID,
            filter={
                "property": "Enabled",
                "checkbox": {"equals": True}
            }
        )
        
        return [
            {
                "url": _get_url_property(item, "Link"),
                "title": _get_title_property(item, "Title")
            }
            for item in response.get("results", [])
        ]
        
    except APIResponseError as e:
        print(f"Notion API error: {e.status} {e.code} - {e.message}")
        return []
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return []

def _get_url_property(item: dict, prop_name: str) -> str:
    """Helper to safely extract URL property"""
    prop = item.get("properties", {}).get(prop_name, {})
    return prop.get("url", "") if prop else "!"

def _get_title_property(item: dict, prop_name: str) -> str:
    """Helper to safely extract title property"""
    title = item.get("properties", {}).get(prop_name, {}).get("title", [])
    return title[0].get("text", {}).get("content", "") if title else "?"