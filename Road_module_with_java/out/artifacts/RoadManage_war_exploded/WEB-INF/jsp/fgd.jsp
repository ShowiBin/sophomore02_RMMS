<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%--
  Created by IntelliJ IDEA.
  User: hp
  Date: 2020/7/5
  Time: 11:22
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Title</title>
    <link href="https://cdn.staticfile.org/twitter-bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
<div class="container">
    <div class="row clearfix">
        <div class="col-md-12 column">
            <div class="page-header">
                <h2><small>分隔带详细信息</small></h2>
            </div>
        </div>

        <div class="row">
            <div class="col-md-1 column">
                <a class="btn btn-primary" href="${pageContext.request.contextPath}/toaddfgd">新增分隔带</a>
            </div>

            <div class="col-md-1 column">
                <a class="btn btn-primary" href="${pageContext.request.contextPath}/todeletefgd">删除已有分隔带</a>
            </div>

            <div class="col-md-10 column">
                <form class="form-inline" action="${pageContext.request.contextPath}/queryfgd" method="post" style="float: right">
                    <input type="text" name="query_road_id" class="form-control" placeholder="请输入要查询的道路id">
                    <input type="submit" name="" value="查询" class="btn btn-primary">
                </form>

            </div>

        </div>



    </div>



    <div class="row clearfix">
        <div class="col-md-12 column">
            <table class="table table-hover">
                <thead>
                <tr>
                    <th>道路编号</th>
                    <th>左中右侧</th>
                    <th>护栏长度</th>
                    <th>护栏高度</th>
                    <th>护栏类型</th>
                    <th>长度</th>
                    <th>宽度范围</th>
                    <th>面积</th>
                    <th>类型</th>
                    <th></th>
                </tr>
                </thead>
                <tbody>
                <c:forEach var="c" items="${list}">
                    <tr>
                        <td>${c.road_id}</td>
                        <td>${c.fgd_zzyc}</td>
                        <td>${c.fgd_hlcd}</td>
                        <td>${c.fgd_hlgd}</td>
                        <td>${c.fgd_hllx}</td>
                        <td>${c.fgd_cd}</td>
                        <td>${c.fgd_kdfw}</td>
                        <td>${c.fgd_mj}</td>
                        <td>${c.fgd_lx}</td>
                        <td>
                            <a href="${pageContext.request.contextPath}/toupdatefgd?id=${c.road_id}&zzyc=${c.fgd_zzyc}">修改</a>
                        </td>
                    </tr>
                </c:forEach>
                </tbody>
            </table>
        </div>
    </div>
</div>
</body>

</html>

