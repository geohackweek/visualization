---
title: "Other Powerful Plotting Tools"
teaching: 10
exercises: 0
questions:
- "What other geospatial visualization tools should I know about?"
objectives: 
- "See how Tableau, GeoViews, and other tools can be used in a data workflow."
---

Sometimes, complex plotting tools in Python aren't precisely the best tool for the job, especially if "the job" is quick and dirty visualization, a more public-facing product, or a visualizing a huge data set. Here I list a couple of other tools which could be useful for other geospatial visualization tasks.

### Tableau

[Tableau](http://tableau.com/) is a robust data visualization software tool, used by businesses, governments, and researchers for myriad data viz purposes. Recently, it has experienced a large growth in [geospatial capability](https://www.tableau.com/solutions/maps). The strength of Tableau is creating visually appealing demonstrations of complicated data in an easy-to-use software program. Here's an example of a Tableau geospatial visualization showing the [history of Wilderness designation](https://public.tableau.com/profile/tony.cannistra#!/vizhome/wildernesses-over-time/TheHistoryofWilderness) in the U.S.:

<div class='tableauPlaceholder' id='viz1536789373846' style='position: relative'><noscript><a href='#'><img alt='The History of Wilderness ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;wi&#47;wildernesses-over-time&#47;TheHistoryofWilderness&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='wildernesses-over-time&#47;TheHistoryofWilderness' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;wi&#47;wildernesses-over-time&#47;TheHistoryofWilderness&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /></object></div><script type='text/javascript'>
var divElement = document.getElementById('viz1536789373846');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='670px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);
</script>


### Holoviews + Geoviews + Datashader

Dealing with a *huge* quantity of geospatial data, and want an interactive visualization? [Holoviews](http://holoviews.org/) is a very powerful data-aware Python visualization library, and has a geospatial component called [GeoViews](http://geoviews.org). They have a great set of tutorials, including one about creating fast, easy to use maps with [huge numbers of data points](http://pyviz.org/tutorial/10_Working_with_Large_Datasets.html). 