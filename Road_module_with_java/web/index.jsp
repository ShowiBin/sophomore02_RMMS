<%--
  Created by IntelliJ IDEA.
  User: hp
  Date: 2020/7/2
  Time: 21:23
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
  <head>
<%--    lalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalala--%>
    <title>城镇道路养护信息管理系统</title>
    <style type="text/css">
        a:hover{display:block;background-color: lightblue}
    </style>
    <link href="https://cdn.staticfile.org/twitter-bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet">
  </head>
  <body>

<%--<div style="height: 15%" >--%>
<%--<h1>请选择内容</h1>--%>
<%--</div>--%>
<div class="text-center">
  <div class="c" style="height: 15%;margin: 20px auto;padding-top:10px;background-color: white" >
    <a href="${pageContext.request.contextPath}/road" style="text-decoration: none;font-size: xx-large";>1.道路</a>
  </div>

  <div class="c" style="height: 15%;margin: 20px auto;padding-top:10px;background-color: white">
    <a href="${pageContext.request.contextPath}/cxd" style="text-decoration: none;font-size: xx-large">2.车行道</a>
  </div>

  <div class="c" style="height: 15%;margin: 20px auto;padding-top:10px;background-color: white">
    <a href="${pageContext.request.contextPath}/fgd" style="text-decoration: none;font-size: xx-large">3.分隔带</a>
  </div>

  <div class="c" style="height: 15%;margin: 20px auto;padding-top:10px;background-color: white">
    <a href="${pageContext.request.contextPath}/rxd" style="text-decoration: none;font-size: xx-large; ">4.人行道</a>
  </div>

  <div class="c" style="height: 15%;margin: 20px auto;padding-top:10px;background-color: white">
    <a href="${pageContext.request.contextPath}/fsss" style="text-decoration: none;font-size: xx-large">5.附属设施</a>
  </div>
</div>

  </body>
</html>
