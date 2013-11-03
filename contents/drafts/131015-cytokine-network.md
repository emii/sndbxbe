Date: 2013-10-15
Title: Cytokine network
Category: projects
Tags: misc
Template: article
Summary: Cytokine network derived from information collected form COPE database

##The whole network

<div class="sigma-parent">
<div class="sigma-expand" id="all-nt">
</div>
</div>
<h2>Our network</h2>
<div class="sigma-parent">
<div class="sigma-expand" id="celltypes-nt">
</div>
</div>
<h2>single network</h2>
<div class="sigma-parent">
<div class="sigma-expand" id="single-nt">
</div>
</div>
<script src="/static/sigma/sigma.min.js"></script>
<script src="/static/sigma/sigma.parseGexf.js"></script>
<script type="text/javascript">
function init() {
      // Instanciate sigma.js and customize rendering:
      var sigInst = sigma.init(document.getElementById('all-nt')).drawingProperties({
        defaultLabelColor: '#333',
        defaultLabelSize: 12,
        defaultLabelBGColor: '#fff',
        defaultLabelHoverColor: '#000',
        labelThreshold: 5,
        defaultEdgeType: 'curve'
      }).graphProperties({
        minNodeSize: 0.5,
        maxNodeSize: 5,
        minEdgeSize: 2,
        maxEdgeSize: 2,
        sideMargin: 50
      }).mouseProperties({
        maxRatio: 32
      });
    
      // Parse a GEXF encoded file to fill the graph
      // (requires "sigma.parseGexf.js" to be included)
      sigInst.parseGexf('/static/data/nt.gexf');
    

    sigInst.bind('overnodes',function(event){
     var nodes = event.content;
     var neighbors = {};
     sigInst.iterEdges(function(e){
        if(nodes.indexOf(e.source)>=0 || nodes.indexOf(e.target)>=0){
             neighbors[e.source] = 1;
             neighbors[e.target] = 1;
        }
     }).iterNodes(function(n){
        if(!neighbors[n.id]){
            n.hidden = 1;
        }else{
            n.hidden = 0;
        }
     }).draw(2,2,2);
    }).bind('outnodes',function(){
        sigInst.iterEdges(function(e){
        e.hidden = 0;
        }).iterNodes(function(n){
            n.hidden = 0;
        }).draw(2,2,2);
    });
     // Draw the graph :
     sigInst.draw();
      
      // Instanciate sigma.js and customize rendering:
      var sigInst2 = sigma.init(document.getElementById('celltypes-nt')).drawingProperties({
        defaultLabelColor: '#333',
        defaultLabelSize: 12,
        defaultLabelBGColor: '#fff',
        defaultLabelHoverColor: '#000',
        labelThreshold: 5,
        defaultEdgeType: 'curve'
      }).graphProperties({
        minNodeSize: 0.5,
        maxNodeSize: 5,
        minEdgeSize: 2,
        maxEdgeSize: 2,
        sideMargin: 50
      }).mouseProperties({
        maxRatio: 32
      });
    
      // Parse a GEXF encoded file to fill the graph
      // (requires "sigma.parseGexf.js" to be included)
      sigInst2.parseGexf('/static/data/nt2.gexf');
    

    sigInst2.bind('overnodes',function(event){
     var nodes = event.content;
     var neighbors = {};
     sigInst2.iterEdges(function(e){
        if(nodes.indexOf(e.source)>=0 || nodes.indexOf(e.target)>=0){
             neighbors[e.source] = 1;
             neighbors[e.target] = 1;
        }
     }).iterNodes(function(n){
        if(!neighbors[n.id]){
            n.hidden = 1;
        }else{
            n.hidden = 0;
        }
     }).draw(2,2,2);
    }).bind('outnodes',function(){
        sigInst2.iterEdges(function(e){
        e.hidden = 0;
        }).iterNodes(function(n){
            n.hidden = 0;
        }).draw(2,2,2);
    });
     // Draw the graph :
     sigInst2.draw();

      // Instanciate sigma.js and customize rendering:
      var sigInst3 = sigma.init(document.getElementById('single-nt')).drawingProperties({
        defaultLabelColor: '#333',
        defaultLabelSize: 12,
        defaultLabelBGColor: '#fff',
        defaultLabelHoverColor: '#000',
        labelThreshold: 5,
        defaultEdgeType: 'curve'
      }).graphProperties({
        minNodeSize: 0.5,
        maxNodeSize: 5,
        minEdgeSize: 2,
        maxEdgeSize: 2,
        sideMargin: 50
      }).mouseProperties({
        maxRatio: 32
      });
    
      // Parse a GEXF encoded file to fill the graph
      // (requires "sigma.parseGexf.js" to be included)
      sigInst3.parseGexf('/static/data/nt3.gexf');
    

     // Draw the graph :
     sigInst3.draw();
}
 
 
if (document.addEventListener) {
  document.addEventListener("DOMContentLoaded", init, false);
} else {
  window.onload = init;
}
</script>

<style type="text/css">
  /* sigma.js context : */
  .sigma-parent {
    position: relative;
    border-radius: 4px;
    -moz-border-radius: 4px;
    -webkit-border-radius: 4px;
    background: #fafafa;
    height: 500px;
	border:1px #bbb solid;
	width: 80%;
	margin: 0 auto;
  }
  .sigma-expand {
    position: absolute;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
  }
  .buttons-container{
    padding-bottom: 8px;
    padding-top: 12px;
  }
</style>
