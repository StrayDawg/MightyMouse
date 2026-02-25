![picture 0](images/c2578cdc2ca5c1ccd8d12ace71e881cd47e47ab97f05ae45bbc0dff0434e6ea7.jpg)  

## Overview

**MightyMouse** is a Python-based automation bot for MyAnonamouse (MAM) that handles torrent management, bonus point optimization, and qBittorrent category organization.

## Key Features

### Torrent Management
- **Unsaturated Torrent Tracking**: Monitors torrents approaching saturation limit and provides warnings with estimated time to completion
- **Automatic Downloads**: Searches for and downloads free/VIP torrents to fill your unsaturated torrent quota
- **Smart Pagination**: Handles large search results across multiple pages to find optimal torrents

### Bonus Point Automation
- **VIP Auto-Purchase**: Automatically buys VIP time when you have sufficient seed bonus points (configurable)
- **Upload Credit Management**: Purchases upload credits as configured
- **Millionaire's Vault Donations**: Auto-donates seed bonus to the vault once per cycle (when eligible)

### qBittorrent Integration
- **Category Management**: Automatically organizes torrents into categories based on saturation status:
  - `MAM_UNSAT`: Unsaturated torrents (actively seeding to saturation)
  - `MAM_SAT`: Saturated torrents (maintenance seeding)
- **Real-time Sync**: Maintains category consistency between MAM data and qBittorrent

### Scheduler
- **Configurable Intervals**: Runs automation at intervals specified in `config.py` (default: 1 hour)
- **Dynamic Scheduling**: Can use STG (Seed To Gain) times to schedule next run based on torrent saturation progress
- **Progress Tracking**: Visual countdown with ETA using `tqdm` progress bar

## Workflow

1. Fetch user profile and statistics from MAM
2. Retrieve unsaturated, saturated, and leeching torrent lists
3. Search for new free/VIP torrents matching your criteria
4. Download torrents in batches (auto-extract if configured)
5. Sync qBittorrent categories with MAM data
6. Auto-purchase VIP/upload credits if configured
7. Auto-donate to Millionaire's Vault if eligible
8. Monitor torrents close to saturation and alert user
9. Schedule next run with countdown timer

## Requirements

- Python 3.8+
- MAM account with valid session ID 
- qBittorrent 
- Dependencies: `requests`, `selenium`, `qbittorrent-api`, `schedule`, `tqdm`

## Configuration

See `config.py` for all available settings including:
- `MAM_ID`: Your MAM session ID
- `RUN_INTERVAL`: Time between automation runs
- `SEARCH`: Torrent search parameters
- `BUY_VIP`, `BUY_UPLOAD`, `DONATE_TO_POT`: Enable/disable automation features
- `QBITTORRENT_*`: Connection details for qBittorrent WebUI

- Sample Output

```
User: ********* - Class: VIP - Bonus Points: 11853
***** Checking Torrent Status *****
You are seeding 146 unsaturated torrents. (Limit: 150 for VIP)
You are seeding 472 saturated torrents
You are leeching 0 torrents
Unsaturated limit not reached: Can get 4 more torrents
User is VIP, searching for free+VIP torrents
getting torrents... 0 - 19
1223304 - Predestination - 629.1 MiB - 0 - 1 - Adding torrent ID
1223303 - Acceptance and Commitment Therapy: 100 Key Points and Techniques, 2nd Edition - 2.6 MiB - 0 - 1 - Adding torrent ID
1223279 - The Nights Are Quiet in Tehran - 634.0 KiB - 0 - 1 - Adding torrent ID
1223278 - A Place Both Wonderful and Strange: The Extraordinary Untold History of Twin Peaks - 26.2 MiB - 0 - 1 - Adding torrent ID
Total torrent IDs fetched: 4
Torrent IDs: ['1223279', '1223304', '1223278', '1223303']
Downloaded: storage\batch_1772028358.6131032.zip
***** Fixing categories in qBittorrent *****
***** Checking VIP Status *****
VIP expires at: 2026-05-25 13:13:18 UTC
VIP time remaining (weeks): 12.709 Purchasable (weeks): 0.148 cost (points): 185.0
Minimum VIP purchase is 1 day, skipping...
Unsaturated torrents sorted by STG (closest to saturation first):
Higher Magic - STG: 2:38 - STG_seconds: 158
Next saturation complete in 158 seconds
***** Fixing categories in qBittorrent *****
Next run scheduled in 458 seconds
```


