{% extends "base.tpl" %}

{% block head %}
    <style type="text/css">
      body {
        padding-top: 20px;
        padding-bottom: 40px;
      }

      /* Custom container */
      .container-narrow {
        margin: 0 auto;
        max-width: 700px;
      }
      .container-narrow > hr {
        margin: 30px 0;
      }

      /* Main marketing message and sign up button */
      .jumbotron {
        margin: 60px 0;
        text-align: center;
      }
      .jumbotron h1 {
        font-size: 72px;
        line-height: 1;
      }
      .jumbotron .btn {
        font-size: 21px;
        padding: 14px 24px;
      }

      /* Supporting marketing content */
      .marketing {
        margin: 60px 0;
      }
      .marketing p + h4 {
        margin-top: 28px;
      }
    </style>

	<script src="http://maps.googleapis.com/maps/api/js?sensor=false&hl=zh-CN&v=3"></script>
	<script src="static/js/angular-google-maps.js"></script>

    {% block app_head %}
    {% end %}
{% end %}

{% block body %}
    <div class="container-narrow">

      <div class="masthead">
        <ul class="nav nav-pills pull-right">
          <li class="active"><a href="#">主页</a></li>
          <li><a href="mailto:godsarmycy@gmail.com">联系我们</a></li>
        </ul>
        <h1 class="muted"><img src="static/img/favicon.png" style="border:10;width:52px;height:52px;"/><a href="/"> {{ project_name }}</a></h1>
      </div>

      <hr>

      {% block container %}
      {% end %}
      
      <hr>

      <div class="footer">
        &copy; Godsarmy 2013
        <div class="pull-right"><a href="http://maps.google.com"><img src="static/img/gmap.png" alt="" style="border:0;width:20px;height:20px;"/></a></div>
        <div class="pull-right"><a href="http://twitter.github.io/bootstrap"><img src="static/img/bootstrap.png" alt="" style="border:0;width:20px;height:20px;"/></a></div>
        <div class="pull-right"><a href="http://www.tornadoweb.org"><img src="static/img/tornado.png" alt="" style="border:0;width:20px;height:20px;"/></a></div>
        <div class="pull-right"><a href="http://angularjs.org"><img src="static/img/AngularJS.png" alt="" style="border:0;width:20px;height:20px;"/></a></div>
        <div class="pull-right"><a href="http://www.mongodb.org"><img src="static/img/mongodb.png" alt="" style="border:0;width:20px;height:20px;"/></a></div>
        <div class="pull-right">Powered by</div>
      </div>

    </div> <!-- /container -->
{% end %}

