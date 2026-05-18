# 🎓 TheTestingAcademy MCP Server

> Built with **FastMCP v3** | Playwright Automation | QA Intelligence

A production-ready Model Context Protocol (MCP) server for AI-assisted Playwright test automation, test management, and QA workflows.

---

## 📁 Project Structure

```
Project21_MCP_VibeCoding/
├── server.py               # Main MCP server (tools, resources, prompts)
├── requirements.txt        # Python dependencies
├── data/
│   ├── __init__.py
│   ├── test_cases.py       # Data 1: 12 dummy test cases
│   └── browser_config.py   # Data 2: Browser & device config profiles
└── README.md
```

---

## ⚙️ Setup

```bash
pip install -r requirements.txt
```

---

## 🚀 Running the Server

```bash
# stdio mode (default for MCP clients like Claude Desktop)
python server.py

# Or explicitly via FastMCP CLI
fastmcp run server.py
```

---

## 🔧 Tools (24)

| # | Tool Name | Description |
|---|-----------|-------------|
| 1 | `launch_browser` | Launch chromium / firefox / webkit |
| 2 | `navigate_to_url` | Navigate to a URL |
| 3 | `click_element` | Click a CSS/XPath selector |
| 4 | `fill_input` | Type into an input field |
| 5 | `take_screenshot` | Capture viewport or full-page screenshot |
| 6 | `get_element_text` | Get inner text of an element |
| 7 | `assert_element_visible` | Assert element is visible |
| 8 | `assert_text_contains` | Assert element text contains a string |
| 9 | `wait_for_selector` | Wait for an element to reach a state |
| 10 | `scroll_to_element` | Scroll element into view |
| 11 | `hover_over_element` | Hover mouse over element |
| 12 | `select_dropdown_option` | Select a `<select>` dropdown option |
| 13 | `press_keyboard_key` | Simulate keyboard key press |
| 14 | `get_page_url` | Get current page URL |
| 15 | `get_page_title` | Get current page title |
| 16 | `close_browser` | Close browser session(s) |
| 17 | `handle_alert` | Accept/dismiss browser alerts |
| 18 | `upload_file` | Upload a file via file input |
| 19 | `get_cookies` | Retrieve browser cookies |
| 20 | `clear_cookies` | Clear all cookies |
| 21 | `execute_javascript` | Run JS in page context |
| 22 | `get_network_requests` | Capture network requests |
| 23 | `run_playwright_test_file` | Run a `.spec.py` test file |
| 24 | `generate_html_report` | Generate HTML test report |

---

## 📦 Resources (3)

| URI | Description |
|-----|-------------|
| `resource://thetestingacademy/test-suite-overview` | Full test suite with modules, owners, statuses |
| `resource://thetestingacademy/playwright-config` | Default `playwright.config` for all projects |
| `resource://thetestingacademy/environment-urls` | Dev / Staging / Production base URLs |

---

## 💾 Data Files (2)

| File | Description |
|------|-------------|
| `data/test_cases.py` | 12 dummy test cases across 7 modules with steps & expected results |
| `data/browser_config.py` | Browser profiles, device emulation, CI settings, network conditions |

---

## 💬 Prompts (5)

| Prompt | Purpose |
|--------|---------|
| `write_playwright_test` | Generate a full POM-based Playwright test script |
| `analyze_test_failure` | Root-cause analysis for a failed test |
| `create_test_plan` | Create a structured QA test plan document |
| `generate_bug_report` | Generate a Jira-ready bug report |
| `review_test_code` | Expert code review of a Playwright test script |

---

## 🔌 Connecting to Claude Desktop

Add to `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "TheTestingAcademy": {
      "command": "python",
      "args": ["e:/Antigravity/Project1_Basics/Project21_MCP_VibeCoding/server.py"]
    }
  }
}
```
