import os
from datetime import datetime

WAVEPLAN_PATH = r"\\ant\dept-eu\Amazon-Flex-Europe\EU-OE\LPnS\LPnS_Model\OptimizedWavePlan.xlsx"
COL_MAP = {
            "Date": "OFD Date",
            "Station": "Station",
            "Wave Start": "Wave",
            "Wave Duration": "Duration",
            "Cycle": "Cycle",
            "Service Type": "Service Type"
        }

BASE_URL = "https://logistics.amazon.co.uk"
SUI_URL = "https://logistics.amazon.co.uk/internal/scheduling/dsps/api/getProviderDemandData"
CAPACITY_UPLOADER_URL = "https://logistics.amazon.co.uk/internal/capacity/uploader"
STATUS_URL = "https://logistics.amazon.co.uk/internal/capacity/api/statusRecordPage"

# User Downloads
LOGIN = os.getlogin()
DOWNLOADS = os.path.join(os.path.expanduser("~"), "Downloads")
COOKIES_FILE = f"mdw_cookie_{datetime.now().strftime("%Y-%m-%d")}.pkl"
COOKIES_PATH = os.path.join(DOWNLOADS, COOKIES_FILE)
SITE_MAP = r"\\ant\dept-eu\TBA\UK\Business Analyses\CentralOPS\Scheduling\UK\FlexData\UKManagedMappings.csv"
SAVE_PATH = os.path.join(DOWNLOADS, "scrape.csv")
STATUS_COLS = ["fileType", "fileName", "uploadedDateTime", "uploadedBy", "status", "message"]