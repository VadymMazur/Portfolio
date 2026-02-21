📑 Comparative Table of Test Documentation Types
| Test Documentation | № | Key Characteristics | Advantages | Disadvantages |
|---------------------|---|---------------------|------------|---------------|
| **Checklist**       | 1 | List of checks      | Structured | Different interpretations of one item |
|                     | 2 | Test environment    | Task understanding | Harder to prove what was tested |
|                     | 3 | Test result         | Saves working time | Difficult to track full requirement coverage |
| **Test Case**       | 1 | Clear detailing     | Reproducibility | Any tester can reproduce a bug | Dependency on previous test case |
|                     | 2 | Steps to reproduce  | Clear structure | Ambiguous wording |
|                     | 3 | Conditions & parameters | Transparency for team and client | Unclear results |
| **Use Case**        | 1 | Interaction between users and application | Gap detection | Does not cover technical details |
|                     | 2 | Covers entire system | User-oriented | Requires additional detailing |

✅ Checklist for Main Page Testing (Example: rozetka.ua)
### General Checks
- Main page opens without errors (404 / 500)
- Correct URL and HTTPS
- Page loads in less than 4 seconds
- No broken elements or empty blocks

### UI / Layout
- Logo displays and links to homepage
- Correct display on different screen resolutions
- No overlapping or misplaced blocks
- Consistent fonts, colors, spacing
- Banners display correctly

### Header
- Search bar is visible
- Search button is active
- Category menu opens
- Login/profile buttons are visible
- Language/region switch works

### Search
- Valid query search works
- Invalid query shows message
- Autocomplete suggestions appear
- Popular product search works

### Categories
- Main categories are visible
- Clicking category leads to correct page
- Dropdown menu works correctly
- No empty categories
- Popular/promotional products are displayed

### Banners / Promotions
- Banners are clickable
- Lead to correct pages
- Match declared promotions
- No broken banners
🧪 Positive Test Cases
### Search for product with valid query
**Precondition:** User on homepage  
**Steps:**  
1. Enter product name (e.g., iPhone)  
2. Click search button  
**Expected Result:** Relevant product list displayed  
**Status:** Not executed  

### Navigate to product category
**Steps:**  
1. Open category menu  
2. Select category (e.g., Smartphones)  
**Expected Result:** Category page opens with products  
**Status:** Pass  

### Open product page
**Steps:**  
1. Click on any product in list  
**Expected Result:** Product page opens with description, prices, offers  
**Status:** Pass  

### Filter products
**Steps:**  
1. Apply filter (brand/price)  
**Expected Result:** Product list updates accordingly  
**Status:** Pass  

### Sort products
**Steps:**  
1. Select sorting (e.g., low to high price)  
**Expected Result:** Products sorted correctly by price  
**Status:** Fail  
🚫 Negative Test Cases
### Search with invalid query
**Steps:**  
1. Enter random symbols (@#$%^)  
2. Click search  
**Expected Result:** "Nothing found" message displayed  
**Status:** Pass  

### Apply filters with no results
**Steps:**  
1. Select mutually exclusive filters  
**Expected Result:** Message about no products found  
**Status:** Pass  

### Navigate to non-existent product page
**Steps:**  
1. Open invalid product URL  
**Expected Result:** 404 page or error message displayed  
**Status:** Not executed  

### Slow image loading
**Steps:**  
1. Open product list  
**Expected Result:** Placeholders/skeletons displayed  
**Status:** Suspended  

### Incorrect sorting behavior
**Steps:**  
1. Apply sorting  
**Expected Result:** Products remain in correct category, filters not reset  
**Status:** Not executed  

