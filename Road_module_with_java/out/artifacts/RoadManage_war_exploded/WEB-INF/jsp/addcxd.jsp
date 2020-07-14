<%--
  Created by IntelliJ IDEA.
  User: hp
  Date: 2020/7/4
  Time: 13:59
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
                <h2><small>新增车行道</small></h2>
            </div>
        </div>
    </div>

    <form action="${pageContext.request.contextPath}/addcxd" method="post">
        <div class="form-group">
            <label>1.道路编号</label>
            <input type="text" name="road_id" class="form-control" required>
        </div>
        <div class="form-group">
            <label>2.路面类型</label>
            <input type="text" name="cxd_lmlx" class="form-control" required>
        </div>
        <div class="form-group">
            <label>3.路面厚度</label>
            <input type="text" name="cxd_lmhd" class="form-control" required>
        </div>
        <div class="form-group">
            <label>4.基层类型</label>
            <input type="text" name="cxd_jclx" class="form-control" required>
        </div>
        <div class="form-group">
            <label>5.基层厚度</label>
            <input type="text" name="cxd_jchd" class="form-control" required>
        </div>
        <div class="form-group">
            <label>6.车道数</label>
            <input type="text" name="cxd_cds" class="form-control" required>
        </div>
        <div class="form-group">
            <label>7.通行方向</label>
            <input type="text" name="cxd_txfx" class="form-control" required>
        </div>
        <div class="form-group">
            <label>8.机动车道宽度范围</label>
            <input type="text" name="cxd_jdcdkdfw" class="form-control" required>
        </div>
        <div class="form-group">
            <label>9.左侧非机动车道宽度范围</label>
            <input type="text" name="cxd_zcfjdcdkdfw" class="form-control" required>
        </div>
        <div class="form-group">
            <label>10.右侧非机动车道宽度范围</label>
            <input type="text" name="cxd_ycfjdcdkdfw" class="form-control" required>
        </div>
        <div class="form-group">
            <label>11.车行道面积</label>
            <input type="text" name="cxd_cxdmj" class="form-control" required>
        </div>
        <div class="form-group">
            <label>12.有无公交车专用道</label>
            <input type="text" name="cxd_ywgjczyd" class="form-control" required>
        </div>
        <div class="form-group">
            <label>13.侧石类型</label>
            <input type="text" name="cxd_cslx" class="form-control" required>
        </div>
        <div class="form-group">
            <label>14.侧石长度</label>
            <input type="text" name="cxd_cscd" class="form-control" required>
        </div>
        <div class="form-group">
            <label>15.平石类型</label>
            <input type="text" name="cxd_pslx" class="form-control" required>
        </div>
        <div class="form-group">
            <label>16.平石长度</label>
            <input type="text" name="cxd_pscd" class="form-control" required>
        </div>
        <div class="form-group">
            <input type="submit" class="form-control" value="添加">
        </div>

    </form>

</div>

</body>
</html>
