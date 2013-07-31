{% extends "app_base.tpl" %}

{% block app_head %}
    <style type="text/css">
        #mapCanvas img {
           max-width: none;
        }
    </style>
{% end %}
{% block container %}
  
<div ng-controller="IndexController">
  <div class="row-fluid">
    {% import time %}
    {% for q in events %}
    <div class="span4">
      <h2>
        <a href="detail?id={{str(q["_id"])}}">{{q["details"]["magnitude"]}} {{q["name"]}}</a>
      </h2>
      <p>
      北京时间 {{time.strftime("%Y-%m-%d %H:%M", time.localtime(q["timestamp"]))}} 
      在{% if "nation" in q %}{{q["nation"]}}{% else %}{{q["name"]}}{% end %}
      ({{q["latitude_type"]}}{{q["latitude_num"]}}, {{q["longitude_type"]}}{{q["longitude_num"]}})
      发生{{q["details"]["magnitude"]}}级地震，震源深度{{q["details"]["depth"]}}公里。
      </p>
      <!--
      <p>
      <a class="btn" href="#">View details »</a>
      </p>
      -->
    </div>        
    {% end %}
  </div>
  <hr>
  <div id="mapCanvas" class="google-map"
		center="centerProperty"
		zoom="zoomProperty" 
		markers="markersProperty"
		latitude="clickedLatitudeProperty"
		longitude="clickedLongitudeProperty"
		draggable="true"
		style="height: 600px; width: 100%">
  </div>
</div>
{% end %}

{% block script %}
    <script type="text/javascript">
       var g_markers = [
           {% for q in events %}
            { latitude: {{q["latitude"]}}, longitude: {{q["longitude"]}} },
           {% end %}
       ];
    </script>
	<script src="static/js/app/index.js"></script>
{% end %}
