<%--
  Created by IntelliJ IDEA.
  User: hp
  Date: 2020/7/6
  Time: 11:52
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
                <h2><small>修改道路信息</small></h2>
            </div>
        </div>
    </div>

    <form action="${pageContext.request.contextPath}/updateroad" method="post">
        <div class="form-group">
            <label>1.道路编号</label>
            <input type="text" name="road_id" class="form-control" value="${q_road.road_id}" required>
        </div>
        <div class="form-group">
            <label>2.道路名称</label>
            <input type="text" name="road_name" class="form-control" value="${q_road.road_name}" required>
        </div>
        <div class="form-group">
            <label>3.道路走向</label>
            <input type="text" name="road_zx" class="form-control" value="${q_road.road_zx}" required>
        </div>
        <div class="form-group">
            <label>4.起点</label>
            <input type="text" name="road_qd" class="form-control" value="${q_road.road_qd}" required>
        </div>
        <div class="form-group">
            <label>5.终点</label>
            <input type="text" name="road_zd" class="form-control" value="${q_road.road_zd}" required>
        </div>
        <div class="form-group">
            <label>6.设计单位</label>
            <input type="text" name="road_sjdw" class="form-control" value="${q_road.road_sjdw}" required>
        </div>
        <div class="form-group">
            <label>7.施工单位</label>
            <input type="text" name="road_sgdw" class="form-control" value="${q_road.road_sgdw}" required>
        </div>
        <div class="form-group">
            <label>8.道路等级</label>
            <input type="text" name="road_dldj" class="form-control" value="${q_road.road_dldj}" required>
        </div>
        <div class="form-group">
            <label>9.路面等级</label>
            <input type="text" name="road_lmdj" class="form-control" value="${q_road.road_lmdj}" required>
        </div>
        <div class="form-group">
            <label>10.设计时速</label>
            <input type="text" name="road_sjss" class="form-control" value="${q_road.road_sjss}" required>
        </div>
        <div class="form-group">
            <label>11.路幅宽度范围</label>
            <input type="text" name="road_lfkdfw" class="form-control" value="${q_road.road_lfkdfw}" required>
        </div>
        <div class="form-group">
            <label>12.道路长度</label>
            <input type="text" name="road_dlcd" class="form-control" value="${q_road.road_dlcd}" required>
        </div>
        <div class="form-group">
            <label>13.道路面积</label>
            <input type="text" name="road_dlmj" class="form-control" value="${q_road.road_dlmj}" required>
        </div>
        <div class="form-group">
            <label>14.AADT</label>
            <input type="text" name="road_AADT" class="form-control" value="${q_road.road_AADT}" required>
        </div>
        <div class="form-group">
            <label>15.交通量等级</label>
            <input type="text" name="road_jtldj" class="form-control" value="${q_road.road_jtldj}" required>
        </div>
        <div class="form-group">
            <label>16.所属乡镇</label>
            <input type="text" name="road_ssxz" class="form-control" value="${q_road.road_ssxz}" required>
        </div>
        <div class="form-group">
            <label>17.管理分类</label>
            <input type="text" name="road_glfl" class="form-control" value="${q_road.road_glfl}" required>
        </div>
        <div class="form-group">
            <label>18.管理单位</label>
            <input type="text" name="road_gldw" class="form-control" value="${q_road.road_gldw}" required>
        </div>
        <div class="form-group">
            <label>19.养护单位</label>
            <input type="text" name="road_yhdw" class="form-control" value="${q_road.road_yhdw}" required>
        </div>
        <div class="form-group">
            <label>20.建造年月</label>
            <input type="text" name="road_jzny" class="form-control" value="${q_road.road_jzny}" required>
        </div>
        <div class="form-group">
            <input type="submit" class="form-control" value="修改">
        </div>

    </form>

</div>

</body>
</html>
