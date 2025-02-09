/src
├── bot/
│   ├── main.py          # Bot initialization and core config
│   ├── constants.py     # Bot constants (colors, IDs, paths)
│   └── utils/          # Utility functions
│       ├── embeds.py    # Embed builders
│       └── helpers.py   # General helper functions
├── cogs/                # Cog-based command modules
│   ├── moderation.py    # Moderation commands/events
│   ├── utilities.py     # Utility commands
│   └── music.py        # Music-related features
├── events/              # Event handlers
│   ├── client/
│   │   ├── on_ready.py
│   │   └── on_connect.py
│   └── guild/
│       ├── on_message.py
│       └── on_member_join.py
└── database/            # Data management
    ├── models.py       # Data models
    └── crud.py         # Database operations
