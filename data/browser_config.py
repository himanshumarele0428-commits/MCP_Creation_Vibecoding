"""
Data File 2: Browser Configuration Profiles
TheTestingAcademy | Playwright Browser & Device Config Data
"""

BROWSER_CONFIG_DATA = {
    "metadata": {
        "source": "TheTestingAcademy DevOps Config Store",
        "version": "2.0.0",
        "last_updated": "2026-05-19"
    },
    "default_settings": {
        "headless": True,
        "slow_mo_ms": 0,
        "timeout_ms": 30000,
        "action_timeout_ms": 10000,
        "navigation_timeout_ms": 30000,
        "screenshot_on_failure": True,
        "video_on_failure": True,
        "trace_on_retry": True
    },
    "browsers": {
        "chromium": {
            "channel": "chrome",
            "viewport": {"width": 1280, "height": 720},
            "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "args": ["--no-sandbox", "--disable-dev-shm-usage"],
            "ignore_https_errors": False
        },
        "firefox": {
            "channel": "firefox",
            "viewport": {"width": 1280, "height": 720},
            "firefox_user_prefs": {"browser.cache.disk.enable": False},
            "ignore_https_errors": False
        },
        "webkit": {
            "channel": "webkit",
            "viewport": {"width": 1280, "height": 720},
            "ignore_https_errors": False
        }
    },
    "device_emulation": {
        "mobile_chrome": {
            "user_agent": "Mozilla/5.0 (Linux; Android 13; Pixel 7)",
            "viewport": {"width": 393, "height": 851},
            "device_scale_factor": 2.75,
            "is_mobile": True,
            "has_touch": True
        },
        "iphone_14": {
            "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X)",
            "viewport": {"width": 390, "height": 844},
            "device_scale_factor": 3,
            "is_mobile": True,
            "has_touch": True
        },
        "ipad_pro": {
            "user_agent": "Mozilla/5.0 (iPad; CPU OS 16_0 like Mac OS X)",
            "viewport": {"width": 1024, "height": 1366},
            "device_scale_factor": 2,
            "is_mobile": True,
            "has_touch": True
        }
    },
    "ci_pipeline_settings": {
        "provider": "GitHub Actions",
        "workers": 4,
        "retries": 2,
        "shard": {"current": 1, "total": 4},
        "reporter": ["github", "html"],
        "artifacts_path": "./test-results",
        "report_path": "./playwright-report"
    },
    "network_conditions": {
        "fast_3g": {
            "download": 1.5e6,
            "upload": 750e3,
            "latency": 40
        },
        "slow_3g": {
            "download": 400e3,
            "upload": 400e3,
            "latency": 200
        },
        "offline": {
            "download": 0,
            "upload": 0,
            "latency": 0
        }
    }
}
