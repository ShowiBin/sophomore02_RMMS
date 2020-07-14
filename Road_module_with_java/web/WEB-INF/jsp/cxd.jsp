<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%--
  Created by IntelliJ IDEA.
  User: hp
  Date: 2020/7/3
  Time: 14:30
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>车行道资料展示</title>
    <link href="https://cdn.staticfile.org/twitter-bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet">

</head>

<body>
<div class="container">
    <div class="row clearfix">
        <div class="col-md-12 column">
            <div class="page-header">
                <h2><small>车行道详细信息</small></h2>
            </div>
        </div>

        <div class="row">
            <div class="col-md-1 column">
                <a class="btn btn-primary" href="${pageContext.request.contextPath}/toaddcxd">新增车行道</a>
            </div>


            <div class="col-md-1 column">
                <a class="btn btn-primary" href="${pageContext.request.contextPath}/todeletecxd">删除已有车行道</a>
            </div>

            <div class="col-md-10 column">
                <form class="form-inline" action="${pageContext.request.contextPath}/queryroad" method="post" style="float: right">
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
                        <th>路面类型</th>
                        <th>路面厚度</th>
                        <th>基层类型</th>
                        <th>基层厚度</th>
                        <th>车道数</th>
                        <th>通行方向</th>
                        <th>机动车道宽度范围</th>
                        <th>左侧机动车道宽度范围</th>
                        <th>右侧机动车道宽度范围</th>
                        <th>车行道面积</th>
                        <th>有无公交车专用道</th>
                        <th>侧石类型</th>
                        <th>侧石长度</th>
                        <th>平石类型</th>
                        <th>平石长度</th>
                        <th>&nbsp;</th>
                    </tr>
                </thead>
                <tbody>

                    <c:forEach var="c" items="${list}">
                        <tr>
                            <td>${c.road_id}</td>
                            <td>${c.cxd_lmlx}</td>
                            <td>${c.cxd_lmhd}</td>
                            <td>${c.cxd_jclx}</td>
                            <td>${c.cxd_jchd}</td>
                            <td>${c.cxd_cds}</td>
                            <td>${c.cxd_txfx}</td>
                            <td>${c.cxd_jdcdkdfw}</td>
                            <td>${c.cxd_zcfjdcdkdfw}</td>
                            <td>${c.cxd_ycfjdcdkdfw}</td>
                            <td>${c.cxd_cxdmj}</td>
                            <td>${c.cxd_ywgjczyd}</td>
                            <td>${c.cxd_cslx}</td>
                            <td>${c.cxd_cscd}</td>
                            <td>${c.cxd_pslx}</td>
                            <td>${c.cxd_pscd}</td>
                            <td>
                                <a href="${pageContext.request.contextPath}/toupdatecxd?id=${c.road_id}">修改</a>
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
