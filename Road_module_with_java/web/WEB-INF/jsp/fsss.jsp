<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%--
  Created by IntelliJ IDEA.
  User: hp
  Date: 2020/7/5
  Time: 15:24
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>附属设施资料展示</title>
    <link href="https://cdn.staticfile.org/twitter-bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet">

</head>

<body>
<div class="container">
    <div class="row clearfix">
        <div class="col-md-12 column">
            <div class="page-header">
                <h2><small>附属设施详细信息</small></h2>
            </div>
        </div>

        <div class="row">
            <div class="col-md-1 column">
                <a class="btn btn-primary" href="${pageContext.request.contextPath}/toaddfsss">新增设施</a>
            </div>


            <div class="col-md-1 column">
                <a class="btn btn-primary" href="${pageContext.request.contextPath}/todeletefsss">删除已有设施</a>
            </div>

            <div class="col-md-10 column">
                <form class="form-inline" action="${pageContext.request.contextPath}/queryfsss" method="post" style="float: right">
                    <input type="text" name="query_road_id" class="form-control" placeholder="请输入要查询的附属设施的道路id">
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
                    <th>检查井数量</th>
                    <th>雨水口数量</th>
                    <th>路名牌数量</th>
                    <th>标志牌数量</th>
                    <th>树池面积</th>
                    <th>其他</th>
                    <th>&nbsp;</th>
                </tr>
                </thead>
                <tbody>

                <c:forEach var="c" items="${list}">
                    <tr>
                        <td>${c.road_id}</td>
                        <td>${c.fsss_jcjsl}</td>
                        <td>${c.fsss_ysksl}</td>
                        <td>${c.fsss_lmpsl}</td>
                        <td>${c.fsss_bzpsl}</td>
                        <td>${c.fsss_scmj}</td>
                        <td>${c.fsss_qt}</td>
                        <td>
                            <a href="${pageContext.request.contextPath}/toupdatefsss?id=${c.road_id}">修改</a>
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

