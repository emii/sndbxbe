Title: Append CSS style
Summary: how to add a css stylesheet using CSS

## Append the follong snnipet at the end of a .md file to include a third css file

	:::html
	<script type="text/javascript">
	  var link = document.createElement("link");
	  link.setAttribute("rel","stylesheet");
	  link.setAttribute("href","http://wherever.com/yourstylesheet.css");
	  var head = document.getElementsByTagName("head")[0];
	  head.appendChild(link);
	</script>

## Or an internal rule within the document head:

	:::html
	<script type="text/javascript">
	  var css = 'h1{color: #ff6600;}',
	  	  style = document.createElement("style"),
	  	  head = document.getElementsByTagName("head")[0];
	  style.setAttribute("type","text/css");
	  style.appendChild(document.createTextNode(css));
	  head.appendChild(style);
	</script>

<script type="text/javascript">
  var css = 'h2{color: #ff6600;}',
  	  style = document.createElement("style"),
  	  head = document.getElementsByTagName("head")[0];
  style.setAttribute("type","text/css");
  style.appendChild(document.createTextNode(css));
  head.appendChild(style);
</script>