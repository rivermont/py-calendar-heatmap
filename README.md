# py-calendar-heatmap
This project will be a Python script (or collection of Python scripts) that will create an svg calendar heatmap - similar to GitHub and others' - from several sources of contribution data.
It will be designed rather specifically around my requirements as it is intended for my personal website, but if someone wants to extend it for more data sources or in some other way, go for it.
Instead of using D3 or other collections of Javascript that need sent to the website viewer, I might just generate a daily svg server-side and include that in the page.
Also, it probably would be faster if written in Go or some other langugage but I know Python so here it is.

![calendar](https://raw.githubusercontent.com/rivermont/py-calendar-heatmap/main/calendar.svg)

### Design
Color scheme will be similar to GitHub's green scale, possibly with a light red for days with 0 contributions (I aim to have contributions on some platform every day).
Hovering over a date square will have either a tooltip or text above/below the heatmap with the date and number of contributions.
Eventually there will be options below the calendar to filter contributions by de/selecting sources.

### Data processing
One part of the script will ingest contribution data from the following sources, parse them, and save them to a single file:
- Git[Hub] commits
- OpenStreetMap changesets
- eBird checklists
- iNaturalist observations
- Observation.org observations
- Mediawiki site edits

Data extracts from these sources are in completely different formats and will be parsed to some standard data structure for the rest of the script to work with.
The only information that needs retained is the date (in local time or UTC?) and the source (for possible filtering later).

<!--maybe use later, once active filtering works
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

