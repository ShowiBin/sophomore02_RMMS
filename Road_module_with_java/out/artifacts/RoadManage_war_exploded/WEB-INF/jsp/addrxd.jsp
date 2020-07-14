<%--
  Created by IntelliJ IDEA.
  User: hp
  Date: 2020/7/6
  Time: 12:50
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title></title>
    <link href="https://cdn.staticfile.org/twitter-bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>

<div class="container">
    <div class="row clearfix">
        <div class="col-md-12 column">
            <div class="page-header">
                <h2><small>新增人行道</small></h2>
            </div>
        </div>
    </div>

    <form action="${pageContext.request.contextPath}/addrxd" method="post">
        <div class="form-group">
            <label>1.道路编号</label>
            <input type="text" name="road_id" class="form-control" required>
        </div>
        <div class="form-group">
            <label>2.左右侧</label>
            <input type="text" name="rxd_zyc" class="form-control" required>
        </div>
        <div class="form-group">
            <label>3.铺面类型</label>
            <input type="text" name="rxd_pmlx" class="form-control" required>
        </div>
        <div class="form-group">
            <label>4.长度</label>
            <input type="text" name="rxd_cd" class="form-control" required>
        </div>
        <div class="form-group">
            <label>5.宽度范围</label>
            <input type="text" name="rxd_kdfw" class="form-control" required>
        </div>
        <div class="form-group">
            <label>6.直线面积</label>
            <input type="text" name="rxd_zxmj" class="form-control" required>
        </div>
        <div class="form-group">
            <label>7.交叉口面积</label>
            <input type="text" name="rxd_jckmj" class="form-control" required>
        </div>
        <div class="form-group">
            <label>8.盲道长度</label>
            <input type="text" name="rxd_mdcd" class="form-control" required>
        </div>
        <div class="form-group">
            <label>9.无障碍通道面积</label>
            <input type="text" name="rxd_wzatdmj" class="form-control" required>
        </div>
        <div class="form-group">
            <label>10.绿化带面积</label>
            <input type="text" name="rxd_lhdmj" class="form-control" required>
        </div>
        <div class="form-group">
            <label>11.侧石类型</label>
            <input type="text" name="rxd_cslx" class="form-control" required>
        </div>
        <div class="form-group">
            <label>12.平石类型</label>
            <input type="text" name="rxd_pslx" class="form-control" required>
        </div>
        <div class="form-group">
            <input type="submit" class="form-control" value="添加">
        </div>

    </form>

</div>
