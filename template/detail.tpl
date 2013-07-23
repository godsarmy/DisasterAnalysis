{% extends "app_base.tpl" %}

{% block app_head %}
    <style type="text/css">
        #mapCanvas img {
           max-width: none;
        }
    </style>
{% end %}

{% block container %}
      <div ng-controller="DetailController">
        <div class="row-fluid">
          <div class="span6">
	        <div id="mapCanvas" class="google-map" 
                center="centerProperty"
                zoom="zoomProperty" 
                markers="markersProperty"
                latitude="clickedLatitudeProperty"
                longitude="clickedLongitudeProperty"
                draggable="true"
                style="height: 400px; width: 100%">
	        </div>
          </div>
          <div class="span6">
            <dl ng-repeat="e in early_events | filter:isCurrent">
              <dt><a href="detail?id={{!e._id}}">{{!e.details.magnitude}} 北京时间 {{!e.strtime}}</a></dt>
              <dd>
              {{!e.name}} ({{!e.latitude_type}}{{!e.latitude_num}}, {{!e.longitude_type}}{{!e.longitude_num}})
              发生{{!e.details.magnitude}}级地震，震源深度{{!e.details.depth}}公里。
              </dd>
            </dl>
            <dl>
              <dt class="text-error">{{event["details"]["magnitude"]}} 北京时间 {{event["strtime"]}}</dt>
              <dd class="text-error">
              {{event["name"]}} ({{event["latitude_type"]}}{{event["latitude_num"]}}, {{event["longitude_type"]}}{{event["longitude_num"]}})
              发生{{event["details"]["magnitude"]}}级地震，震源深度{{event["details"]["depth"]}}公里。
              </dd>
            </dl>
            <dl ng-repeat="e in late_events">
              <dt><a href="detail?id={{!e._id}}">{{!e.details.magnitude}} 北京时间 {{!e.strtime}}</a></dt>
              <dd>
              {{!e.name}} ({{!e.latitude_type}}{{!e.latitude_num}}, {{!e.longitude_type}}{{!e.longitude_num}})
              发生{{!e.details.magnitude}}级地震，震源深度{{!e.details.depth}}公里。
              </dd>
            </dl>
            </dl>
          </div>
        </div>
      </div>
{% end %}

{% block script %}
    <script type="text/javascript">
       var g_markers = [
            { latitude: {{event["latitude"]}}, longitude: {{event["longitude"]}} }
       ];
       var g_longitude = {{event["longitude"]}};
       var g_latitude = {{event["latitude"]}};

       var g_oid = "{{str(event["_id"])}}";
       var g_timestamp = {{event["timestamp"]}};
    </script>
	<script src="static/js/app/detail.js"></script>
{% end %}
