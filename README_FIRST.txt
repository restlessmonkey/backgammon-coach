BACKGAMMON COACH — IPHONE INSTALLABLE WEB APP

This folder must be published as a website before iPhone Safari can install it.
Do not open index.html directly from the Files app.

EASIEST PUBLISHING METHOD (computer recommended)
1. Sign in to Netlify.
2. Open https://app.netlify.com/drop
3. Drag the entire Backgammon_Coach_iPhone_PWA folder into the drop area.
4. Netlify will provide an https://...netlify.app address.
5. Open that address in Safari on your iPhone.
6. Tap Safari's Share button.
7. Tap Add to Home Screen, then Add.
8. Launch Backgammon Coach from its new Home Screen icon.

OFFLINE USE
Open the installed app once while online. The included service worker then caches
its files so it can ordinarily reopen without an internet connection.

UPDATING
Edit or replace the files, then deploy the folder again in Netlify. The service
worker cache name may be increased when releasing a changed version.


VERSION 1.4 CHANGES
- Added Undo for the human player during the current turn.
- Undo is disabled during computer play.
- Moved the turn-status banner above the board so it no longer covers pip/checker areas.
