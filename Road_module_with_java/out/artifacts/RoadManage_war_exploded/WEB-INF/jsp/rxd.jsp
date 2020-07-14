<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%--
  Created by IntelliJ IDEA.
  User: hp
  Date: 2020/7/6
  Time: 13:08
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>人行道资料展示</title>
    <link href="https://cdn.staticfile.org/twitter-bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet">

</head>

<body>
<div class="container">
    <div class="row clearfix">
        <div class="col-md-12 column">
            <div class="page-header">
                <h2><small>人行道详细信息</small></h2>
            </div>
        </div>

        <div class="row">
            <div class="col-md-1 column">
                <a class="btn btn-primary" href="${pageContext.request.contextPath}/toaddrxd">新增人行道</a>
            </div>


            <div class="col-md-1 column">
                <a class="btn btn-primary" href="${pageContext.request.contextPath}/todeleterxd">删除已有人行道</a>
            </div>

            <div class="col-md-10 column">
                <form class="form-inline" action="${pageContext.request.contextPath}/queryrxd" method="post" style="float: right">
                    <input type="text" name="query_road_id" class="form-control" placeholder="请输入要查询的人行道的道路id">
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
                        <th>左右侧</th>
                        <th>铺面类型</th>
                        <th>长度</th>
                        <th>宽度范围</th>
                        <th>直线面积</th>
                        <th>交叉口面积</th>
                        <th>盲道长度</th>
                        <th>无障碍通道面积</th>
                        <th>绿化带面积</th>
                        <th>侧石类型</th>
                        <th>平石类型</th>
                        <th>&nbsp;</th>
                    </tr>
                </thead>
                <tbody>

                <c:forEach var="c" items="${list}">
                    <tr>
                        <td>${c.road_id}</td>
                        <td>${c.rxd_zyc}</td>
                        <td>${c.rxd_pmlx}</td>
                        <td>${c.rxd_cd}</td>
                        <td>${c.rxd_kdfw}</td>
                        <td>${c.rxd_zxmj}</td>
                        <td>${c.rxd_jckmj}</td>
                        <td>${c.rxd_mdcd}</td>
                        <td>${c.rxd_wzatdmj}</td>
                        <td>${c.rxd_lhdmj}</td>
                        <td>${c.rxd_cslx}</td>
                        <td>${c.rxd_pslx}</td>
                        <td>
                            <a href="${pageContext.request.contextPath}/toupdaterxd?id=${c.road_id}&rxd_zyc=${c.rxd_zyc}">修改</a>
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
