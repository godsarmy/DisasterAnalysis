{% extends "app_base.tpl" %}

{% block app_head %}
    <style type="text/css">
        #mapCanvas img {
           max-width: none;
        }
    </style>
{% end %}
{% block container %}
  
<div ng-controller="StatisticController">
</div>
{% end %}

{% block script %}
	<script src="static/js/app/statistics.js"></script>
{% end %}
