import logging
import asyncio

from sui_scrape.site_scrape import SiteScraper, main as run_scraper
from sui_scrape.cookie_scrape import Cookies
from sa_output.get_output import SaOutput
from config import *

# Configure logging to emit to terminal
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logger = logging.getLogger(__name__)

def main() -> None:

    # Use scraper to scrape site data
    logger.info("Starting site scraper...")
    asyncio.run(run_scraper())

    # Get current SA Output
    logger.info("Processing SA outputs...")
    sa = SaOutput(wave_plan_path=WAVEPLAN_PATH, next_week=True)
    waveplan = sa.read_waveplan()
    sa_output = sa.get_sa_outputs(waveplan)
    logger.info("Saving SA to Downloads folder...")
    sa_output.to_csv(os.path.join(DOWNLOADS, "sa_output.csv"))

    # Subtract accepted offers from SA Outputs

    # Save cleaned SA Output



if __name__ == "__main__":
    main()