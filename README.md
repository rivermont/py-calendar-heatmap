# py-calendar-heatmap
Generate an svg calendar heatmap - similar to GitHub and others' - from several sources of contribution data.

![calendar](https://raw.githubusercontent.com/rivermont/py-calendar-heatmap/main/calendar.svg)

### Usage
- Supports contributions from GitHub, eBird (checklists), iNaturalist and Observation.org (observations), and OpenStreetMap (changesets).
- Copy data exports from the first three to a `data` folder, and update the function parameters at the end of `parse.py`.
- Run `parse` and then `main.py` to generate the svg output, which can then be included in a webpage as an `img` or `object`.

Hovering over a date square will have either a tooltip or text above/below the heatmap with the date and number of contributions.

### Future improvements
- Add processing for edits from Mediawiki sites
- Eventually there will be options below the calendar to filter contributions by de/selecting sources.

<!--maybe use later, once active filtering works:
#### Data format
```json
[
{"date": "2022-01-01", "git": "2", "osm": "23", "ebird": "1", "inat": "0", "obs": "0", "mw": "1"},
{"date": "2022-01-02", "git": "0", "osm": "3", "ebird": "2", "inat": "1", "obs": "0", "mw": "0"}
]

```
-->

<!--
```javascript
// init()
  // create empty calendar from current date - 365 days

// Read in data from file

// Output svg or html content to document

// on checkbox change
function updateCal() {
  // check which boxes are checked
  document.getElementsByClassName(".cb");
  // refresh calendar with totals from checked sources
}
```
-->
<!--checkbox for filtering:
<input type="checkbox" class="cb" onchange="updateCal()" />
-->
