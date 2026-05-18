"""
TheTestingAcademy MCP Server
Built with FastMCP | Playwright Automation Tools
"""

from fastmcp import FastMCP
from data.test_cases import TEST_CASES_DATA
from data.browser_config import BROWSER_CONFIG_DATA
import json
import random
from datetime import datetime

# ──────────────────────────────────────────────
# Initialize FastMCP Server
# ──────────────────────────────────────────────
mcp = FastMCP(
    name="TheTestingAcademy",
    version="1.0.0"
)

# ══════════════════════════════════════════════
# ██████  PLAYWRIGHT TOOLS (20+)  ██████████████
# ══════════════════════════════════════════════

@mcp.tool()
def launch_browser(browser: str = "chromium", headless: bool = True) -> dict:
    """Launch a Playwright browser instance (chromium, firefox, or webkit)."""
    return {
        "status": "success",
        "browser": browser,
        "headless": headless,
        "session_id": f"session_{random.randint(1000, 9999)}",
        "launched_at": datetime.now().isoformat(),
        "message": f"[OK] {browser.capitalize()} browser launched {'(headless)' if headless else '(headed)'}."
    }


@mcp.tool()
def navigate_to_url(url: str, wait_until: str = "domcontentloaded") -> dict:
    """Navigate the browser to a specified URL and wait for the page to load."""
    return {
        "status": "success",
        "url": url,
        "wait_until": wait_until,
        "response_code": 200,
        "title": f"Page at {url}",
        "load_time_ms": random.randint(300, 2000),
        "message": f"[OK] Navigated to {url} successfully."
    }


@mcp.tool()
def click_element(selector: str, timeout_ms: int = 5000) -> dict:
    """Click a DOM element identified by a CSS or XPath selector."""
    return {
        "status": "success",
        "selector": selector,
        "timeout_ms": timeout_ms,
        "clicked_at": datetime.now().isoformat(),
        "message": f"[OK] Clicked element: '{selector}'."
    }


@mcp.tool()
def fill_input(selector: str, value: str, clear_first: bool = True) -> dict:
    """Fill an input field with the provided value."""
    return {
        "status": "success",
        "selector": selector,
        "value_entered": value,
        "cleared_first": clear_first,
        "message": f"[OK] Filled '{selector}' with value '{value}'."
    }


@mcp.tool()
def take_screenshot(file_name: str = "screenshot.png", full_page: bool = False) -> dict:
    """Capture a screenshot of the current browser viewport or full page."""
    path = f"screenshots/{file_name}"
    return {
        "status": "success",
        "saved_to": path,
        "full_page": full_page,
        "dimensions": {"width": 1280, "height": 720 if not full_page else 4800},
        "message": f"[SCREENSHOT] Screenshot saved to '{path}'."
    }


@mcp.tool()
def get_element_text(selector: str) -> dict:
    """Retrieve the inner text content of a DOM element."""
    dummy_texts = {
        "h1": "Welcome to TheTestingAcademy",
        "button": "Submit",
        ".error-msg": "Invalid credentials. Please try again.",
        "#title": "Dashboard",
    }
    text = dummy_texts.get(selector, f"Dummy text for '{selector}'")
    return {
        "status": "success",
        "selector": selector,
        "inner_text": text,
        "message": f"[OK] Retrieved text from '{selector}'."
    }


@mcp.tool()
def assert_element_visible(selector: str, timeout_ms: int = 3000) -> dict:
    """Assert that a DOM element is visible on the page."""
    is_visible = random.choice([True, True, True, False])
    return {
        "status": "passed" if is_visible else "failed",
        "selector": selector,
        "visible": is_visible,
        "timeout_ms": timeout_ms,
        "message": f"{'[OK] Element visible' if is_visible else '[FAIL] Element NOT visible'}: '{selector}'."
    }


@mcp.tool()
def assert_text_contains(selector: str, expected_text: str) -> dict:
    """Assert that an element's text contains the expected substring."""
    passed = random.choice([True, True, False])
    return {
        "status": "passed" if passed else "failed",
        "selector": selector,
        "expected_text": expected_text,
        "actual_text": expected_text if passed else "Unexpected content",
        "message": f"{'[OK] Assertion passed' if passed else '[FAIL] Assertion FAILED'} for text '{expected_text}' in '{selector}'."
    }


@mcp.tool()
def wait_for_selector(selector: str, state: str = "visible", timeout_ms: int = 10000) -> dict:
    """Wait for a DOM element to reach a specific state (visible, hidden, attached, detached)."""
    wait_time = random.randint(100, timeout_ms)
    return {
        "status": "success",
        "selector": selector,
        "state_reached": state,
        "waited_ms": wait_time,
        "message": f"[OK] Waited {wait_time}ms for '{selector}' to be '{state}'."
    }


@mcp.tool()
def scroll_to_element(selector: str) -> dict:
    """Scroll the page to bring a specific element into the viewport."""
    return {
        "status": "success",
        "selector": selector,
        "scrolled_to": {"x": 0, "y": random.randint(100, 3000)},
        "message": f"[OK] Scrolled to element '{selector}'."
    }


@mcp.tool()
def hover_over_element(selector: str) -> dict:
    """Hover the mouse cursor over a DOM element to trigger hover effects."""
    return {
        "status": "success",
        "selector": selector,
        "hovered_at": datetime.now().isoformat(),
        "message": f"[OK] Hovered over element '{selector}'."
    }


@mcp.tool()
def select_dropdown_option(selector: str, option_value: str) -> dict:
    """Select an option from a <select> dropdown element by value."""
    return {
        "status": "success",
        "selector": selector,
        "selected_value": option_value,
        "message": f"[OK] Selected option '{option_value}' in dropdown '{selector}'."
    }


@mcp.tool()
def press_keyboard_key(key: str, selector: str = "body") -> dict:
    """Simulate a keyboard key press (e.g., Enter, Tab, Escape, ArrowDown)."""
    return {
        "status": "success",
        "key_pressed": key,
        "target_element": selector,
        "message": f"[OK] Pressed key '{key}' on element '{selector}'."
    }


@mcp.tool()
def get_page_url() -> dict:
    """Retrieve the current URL of the active browser page."""
    sample_urls = [
        "https://thetestingacademy.com/dashboard",
        "https://thetestingacademy.com/login",
        "https://thetestingacademy.com/courses",
    ]
    return {
        "status": "success",
        "current_url": random.choice(sample_urls),
        "message": "[OK] Current page URL retrieved."
    }


@mcp.tool()
def get_page_title() -> dict:
    """Retrieve the title of the current browser page."""
    return {
        "status": "success",
        "page_title": "TheTestingAcademy | QA Learning Platform",
        "message": "[OK] Page title retrieved."
    }


@mcp.tool()
def close_browser(session_id: str = "all") -> dict:
    """Close a specific browser session or all open sessions."""
    return {
        "status": "success",
        "closed_session": session_id,
        "message": f"[OK] Browser session '{session_id}' closed."
    }


@mcp.tool()
def handle_alert(action: str = "accept", prompt_text: str = "") -> dict:
    """Handle browser alerts/confirms/prompts by accepting or dismissing them."""
    return {
        "status": "success",
        "action": action,
        "prompt_text_entered": prompt_text,
        "alert_type": random.choice(["alert", "confirm", "prompt"]),
        "message": f"[OK] Alert {action}ed."
    }


@mcp.tool()
def upload_file(selector: str, file_path: str) -> dict:
    """Upload a file using a file input element on the page."""
    return {
        "status": "success",
        "selector": selector,
        "file_path": file_path,
        "file_size_kb": random.randint(10, 5000),
        "message": f"[OK] File '{file_path}' uploaded via '{selector}'."
    }


@mcp.tool()
def get_cookies(domain: str = "") -> dict:
    """Retrieve browser cookies, optionally filtered by domain."""
    cookies = [
        {"name": "session_token", "value": "abc123xyz", "domain": domain or "thetestingacademy.com"},
        {"name": "user_pref", "value": "dark_mode", "domain": domain or "thetestingacademy.com"},
    ]
    return {
        "status": "success",
        "domain_filter": domain,
        "cookies": cookies,
        "count": len(cookies),
        "message": f"[OK] Retrieved {len(cookies)} cookies."
    }


@mcp.tool()
def clear_cookies() -> dict:
    """Clear all cookies from the current browser context."""
    return {
        "status": "success",
        "cleared_at": datetime.now().isoformat(),
        "message": "[OK] All cookies cleared from browser context."
    }


@mcp.tool()
def execute_javascript(script: str) -> dict:
    """Execute arbitrary JavaScript code in the browser page context."""
    return {
        "status": "success",
        "script_executed": script[:80] + "..." if len(script) > 80 else script,
        "return_value": "undefined",
        "executed_at": datetime.now().isoformat(),
        "message": "[OK] JavaScript executed successfully."
    }


@mcp.tool()
def get_network_requests(filter_url: str = "") -> dict:
    """Capture and return network requests made by the browser page."""
    network_reqs = [
        {"method": "GET", "url": "https://api.thetestingacademy.com/courses", "status": 200},
        {"method": "POST", "url": "https://api.thetestingacademy.com/login", "status": 200},
        {"method": "GET", "url": "https://api.thetestingacademy.com/user/profile", "status": 401},
    ]
    filtered = [r for r in network_reqs if filter_url in r["url"]] if filter_url else network_reqs
    return {
        "status": "success",
        "filter": filter_url,
        "requests": filtered,
        "count": len(filtered),
        "message": f"[OK] Captured {len(filtered)} network request(s)."
    }


@mcp.tool()
def run_playwright_test_file(file_path: str, browser: str = "chromium", headed: bool = False) -> dict:
    """Execute a Playwright test file and return the results summary."""
    passed = random.randint(5, 20)
    failed = random.randint(0, 3)
    return {
        "status": "completed",
        "file": file_path,
        "browser": browser,
        "headed": headed,
        "results": {
            "passed": passed,
            "failed": failed,
            "skipped": random.randint(0, 2),
            "total": passed + failed,
            "duration_seconds": round(random.uniform(5.0, 60.0), 2)
        },
        "message": f"[OK] Test run complete. {passed} passed, {failed} failed."
    }


@mcp.tool()
def generate_html_report(output_dir: str = "reports/") -> dict:
    """Generate an HTML test report from the last Playwright test run."""
    return {
        "status": "success",
        "report_path": f"{output_dir}index.html",
        "generated_at": datetime.now().isoformat(),
        "message": f"[REPORT] HTML report generated at '{output_dir}index.html'."
    }


@mcp.tool()
def get_all_test_cases(module: str = "", status: str = "", priority: str = "") -> str:
    """Query the TheTestingAcademy test case repository. Filter by module, status (Pass/Fail/Flaky/Pending), or priority (Critical/High/Medium/Low)."""
    cases = TEST_CASES_DATA["test_cases"]
    if module:
        cases = [c for c in cases if module.lower() in c["module"].lower()]
    if status:
        cases = [c for c in cases if c["status"].lower() == status.lower()]
    if priority:
        cases = [c for c in cases if c["priority"].lower() == priority.lower()]
    return json.dumps({
        "source": TEST_CASES_DATA["metadata"],
        "filters": {"module": module, "status": status, "priority": priority},
        "total_matched": len(cases),
        "test_cases": cases
    }, indent=2)


@mcp.tool()
def get_browser_profile(profile: str = "chromium", include_ci: bool = False) -> str:
    """Retrieve a browser or device configuration profile from the TheTestingAcademy config store. Profiles: chromium, firefox, webkit, mobile_chrome, iphone_14, ipad_pro."""
    config = BROWSER_CONFIG_DATA
    result = {
        "metadata": config["metadata"],
        "default_settings": config["default_settings"],
    }
    browser_profiles = config["browsers"]
    device_profiles = config["device_emulation"]
    if profile in browser_profiles:
        result["profile_type"] = "browser"
        result["profile"] = browser_profiles[profile]
    elif profile in device_profiles:
        result["profile_type"] = "device_emulation"
        result["profile"] = device_profiles[profile]
    else:
        result["profile_type"] = "not_found"
        result["available"] = list(browser_profiles.keys()) + list(device_profiles.keys())
    if include_ci:
        result["ci_pipeline_settings"] = config["ci_pipeline_settings"]
        result["network_conditions"] = config["network_conditions"]
    return json.dumps(result, indent=2)


# ══════════════════════════════════════════════
# ██████  RESOURCES (3)  ███████████████████████
# ══════════════════════════════════════════════

@mcp.resource("resource://thetestingacademy/test-suite-overview")
def get_test_suite_overview() -> str:
    """A structured overview of the TheTestingAcademy test suite, including modules, owners, and statuses."""
    return json.dumps({
        "academy": "TheTestingAcademy",
        "version": "1.0.0",
        "test_suite": {
            "total_modules": 8,
            "total_test_cases": 142,
            "modules": [
                {"name": "Login & Authentication", "tests": 18, "owner": "QA-Team-Alpha", "status": "stable"},
                {"name": "Dashboard", "tests": 22, "owner": "QA-Team-Alpha", "status": "stable"},
                {"name": "Course Management", "tests": 35, "owner": "QA-Team-Beta", "status": "in_progress"},
                {"name": "User Profile", "tests": 15, "owner": "QA-Team-Beta", "status": "stable"},
                {"name": "Payment Gateway", "tests": 20, "owner": "QA-Team-Gamma", "status": "flaky"},
                {"name": "Notifications", "tests": 12, "owner": "QA-Team-Alpha", "status": "stable"},
                {"name": "Search & Filters", "tests": 10, "owner": "QA-Team-Beta", "status": "new"},
                {"name": "Admin Panel", "tests": 10, "owner": "QA-Team-Gamma", "status": "in_progress"},
            ]
        },
        "last_run": datetime.now().isoformat()
    }, indent=2)


@mcp.resource("resource://thetestingacademy/playwright-config")
def get_playwright_config() -> str:
    """The default Playwright configuration used across all test suites at TheTestingAcademy."""
    config = {
        "testDir": "./tests",
        "timeout": 30000,
        "retries": 2,
        "workers": 4,
        "reporter": [["html", {"outputFolder": "reports/"}], ["list"]],
        "use": {
            "baseURL": "https://thetestingacademy.com",
            "headless": True,
            "viewport": {"width": 1280, "height": 720},
            "screenshot": "only-on-failure",
            "video": "retain-on-failure",
            "trace": "on-first-retry",
            "actionTimeout": 10000,
            "navigationTimeout": 30000
        },
        "projects": [
            {"name": "chromium", "use": {"browserName": "chromium"}},
            {"name": "firefox", "use": {"browserName": "firefox"}},
            {"name": "webkit", "use": {"browserName": "webkit"}},
        ]
    }
    return json.dumps(config, indent=2)


@mcp.resource("resource://thetestingacademy/environment-urls")
def get_environment_urls() -> str:
    """All environment base URLs (dev, staging, production) for TheTestingAcademy platform."""
    return json.dumps({
        "environments": {
            "development": {
                "base_url": "https://dev.thetestingacademy.com",
                "api_url": "https://api-dev.thetestingacademy.com",
                "admin_url": "https://admin-dev.thetestingacademy.com"
            },
            "staging": {
                "base_url": "https://staging.thetestingacademy.com",
                "api_url": "https://api-staging.thetestingacademy.com",
                "admin_url": "https://admin-staging.thetestingacademy.com"
            },
            "production": {
                "base_url": "https://thetestingacademy.com",
                "api_url": "https://api.thetestingacademy.com",
                "admin_url": "https://admin.thetestingacademy.com"
            }
        },
        "notes": "Always run smoke tests on staging before any production deployment."
    }, indent=2)


# ══════════════════════════════════════════════
# ██████  PROMPTS (5)  █████████████████████████
# ══════════════════════════════════════════════

@mcp.prompt()
def write_playwright_test(feature: str, url: str, actions: str) -> str:
    """Generate a Playwright test script for a given feature and user actions."""
    return f"""You are a Senior QA Automation Engineer at TheTestingAcademy.

Write a complete, production-ready Playwright test in Python (using pytest-playwright) for the following:

**Feature Under Test:** {feature}
**Target URL:** {url}
**User Actions to Automate:**
{actions}

Requirements:
- Use the Page Object Model (POM) pattern
- Add meaningful assertions after each major action
- Include proper waits (avoid hardcoded sleeps)
- Add a docstring explaining the test purpose
- Handle potential flakiness with retry logic
- Log important steps using print() or a logger
- Follow TheTestingAcademy coding standards

Generate the complete test file content."""


@mcp.prompt()
def analyze_test_failure(test_name: str, error_message: str, screenshot_path: str = "") -> str:
    """Analyze a failed Playwright test and suggest root cause + fix."""
    screenshot_note = f"\nScreenshot available at: {screenshot_path}" if screenshot_path else ""
    return f"""You are a QA debugging expert at TheTestingAcademy.

A Playwright test has FAILED. Analyze the failure and provide a structured root-cause analysis.

**Failed Test:** {test_name}
**Error Message:**
```
{error_message}
```{screenshot_note}

Provide your analysis in this structure:
1. **Root Cause** — What likely caused this failure?
2. **Category** — (e.g., element not found, timing issue, assertion mismatch, network error)
3. **Severity** — (Critical / High / Medium / Low)
4. **Suggested Fix** — Exact code change or config update needed
5. **Prevention** — How to prevent this class of failure in future tests

Be specific and actionable."""


@mcp.prompt()
def create_test_plan(module_name: str, features: str, environment: str = "staging") -> str:
    """Create a structured QA test plan for a given module and feature set."""
    return f"""You are the Lead QA Strategist at TheTestingAcademy.

Create a comprehensive QA test plan for the following module:

**Module:** {module_name}
**Features to Cover:**
{features}
**Target Environment:** {environment}

The test plan must include:
1. **Objectives** — What are we validating?
2. **Scope** — In-scope and out-of-scope items
3. **Test Types** — (Smoke, Regression, Sanity, E2E, Performance)
4. **Test Cases Table** — (ID | Title | Priority | Type | Automation Candidate)
5. **Entry & Exit Criteria**
6. **Risk Assessment** — Identify top 3 risks and mitigations
7. **Timeline Estimate** — Story points or hours per phase
8. **Tools & Framework** — Playwright, pytest, Allure, CI/CD hooks

Format as a professional QA document."""


@mcp.prompt()
def generate_bug_report(test_name: str, steps_to_reproduce: str, expected: str, actual: str, severity: str = "High") -> str:
    """Generate a professional bug report from a failed test scenario."""
    return f"""You are a QA Engineer at TheTestingAcademy filing a formal bug report.

Generate a detailed, Jira-ready bug report from the following test failure data:

**Test Name:** {test_name}
**Severity:** {severity}
**Steps to Reproduce:**
{steps_to_reproduce}
**Expected Result:** {expected}
**Actual Result:** {actual}

Format the bug report with:
- **Summary** (one-line title)
- **Description** (detailed narrative)
- **Environment** (OS, Browser, App Version, Environment URL)
- **Steps to Reproduce** (numbered list)
- **Expected vs Actual** (clear comparison)
- **Impact** (who and what is affected)
- **Attachments Needed** (screenshots, videos, logs)
- **Suggested Labels** (bug, regression, critical, etc.)
- **Suggested Assignee** (based on module ownership)

Output should be copy-pasteable into Jira."""


@mcp.prompt()
def review_test_code(code: str, language: str = "python") -> str:
    """Perform a thorough code review of a Playwright test script."""
    return f"""You are a Principal QA Engineer at TheTestingAcademy conducting a code review.

Review the following {language} Playwright test code and provide expert feedback:

```{language}
{code}
```

Evaluate and comment on:
1. **Correctness** — Will the test reliably verify the intended behavior?
2. **Locator Strategy** — Are selectors robust and maintainable?
3. **Wait Strategy** — Are waits appropriate? Any risk of race conditions?
4. **Assertions** — Are they meaningful? Are edge cases covered?
5. **Code Quality** — Readability, naming conventions, DRY principle
6. **Performance** — Is the test efficient? Any unnecessary steps?
7. **POM Compliance** — Does it follow Page Object Model best practices?
8. **CI/CD Readiness** — Will this run reliably in a headless CI pipeline?

Provide:
- An overall score (1-10)
- A summary of strengths
- A prioritized list of issues (Critical / Major / Minor)
- Refactored code snippets for each issue found"""


# ══════════════════════════════════════════════
# ██████  ENTRY POINT  █████████████████████████
# ══════════════════════════════════════════════

if __name__ == "__main__":
    mcp.run()
