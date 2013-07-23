<!DOCTYPE html>
<html lang="en">
  <head>
    <link rel="icon" type="image/png" href="static/img/favicon.png">
    <meta charset="utf-8">
    <title>{{project_name}}</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="">

    <!-- Le styles, please change the css url to local relative path -->
    <link href="static/css/bootstrap.min.css" rel="stylesheet">
    <link href="static/css/bootstrap-responsive.css" rel="stylesheet">

    <!-- HTML5 shim, for IE6-8 support of HTML5 elements -->
    <!--<script src="static/js/html5shiv.js"></script>-->

    <!-- Fav and touch icons, please change the css url to local relative path -->
    <link rel="apple-touch-icon-precomposed" sizes="144x144" href="http://twitter.github.com/bootstrap/assets/ico/apple-touch-icon-144-precomposed.png">
    <link rel="apple-touch-icon-precomposed" sizes="114x114" href="http://twitter.github.com/bootstrap/assets/ico/apple-touch-icon-114-precomposed.png">
      <link rel="apple-touch-icon-precomposed" sizes="72x72" href="http://twitter.github.com/bootstrap/assets/ico/apple-touch-icon-72-precomposed.png">
                    <link rel="apple-touch-icon-precomposed" href="http://twitter.github.com/bootstrap/assets/ico/apple-touch-icon-57-precomposed.png">
                                   <link rel="shortcut icon" href="static/favicon.ico">

    <!-- jquery js and js for angularJS from github -->
    <script src="static/js/jquery.min.js"></script>
    <script src="static/js/angular.min.js"></script>

    {% block head %}
    {% end %}
  </head>

  <body ng-app={{app_name}}>

    {% block body %}
    {% end %}

    <!-- Le javascript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster, please change the css url to local relative path -->
    <script src="static/js/bootstrap.min.js"></script>

    {% block script %}
    {% end %}
  </body>
</html>
