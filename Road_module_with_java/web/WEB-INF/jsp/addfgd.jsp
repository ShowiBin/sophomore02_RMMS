<%--
  Created by IntelliJ IDEA.
  User: hp
  Date: 2020/7/5
  Time: 12:13
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
                <h2><small>新增分隔带</small></h2>
            </div>
        </div>
    </div>

    <form action="${pageContext.request.contextPath}/addfgd" method="post">
        <div class="form-group">
            <label>1.道路编号</label>
            <input type="text" name="road_id" class="form-control" required>
        </div>
        <div class="form-group">
            <label>2.左中右侧</label>
            <input type="text" name="fgd_zzyc" class="form-control" required>
        </div>
        <div class="form-group">
            <label>3.护栏长度</label>
            <input type="text" name="fgd_hlcd" class="form-control" required>
        </div>
        <div class="form-group">
            <label>4.护栏高度</label>
            <input type="text" name="fgd_hlgd" class="form-control" required>
        </div>
        <div class="form-group">
            <label>5.护栏类型</label>
            <input type="text" name="fgd_hllx" class="form-control" required>
        </div>
        <div class="form-group">
            <label>6.长度</label>
            <input type="text" name="fgd_cd" class="form-control" required>
        </div>
        <div class="form-group">
            <label>7.宽度范围</label>
            <input type="text" name="fgd_kdfw" class="form-control" required>
        </div>
        <div class="form-group">
            <label>8.面积</label>
            <input type="text" name="fgd_mj" class="form-control" required>
        </div>
        <div class="form-group">
            <label>9.类型</label>
            <input type="text" name="fgd_lx" class="form-control" required>
        </div>
        <div class="form-group">
            <input type="submit" class="form-control" value="添加">
        </div>

    </form>

</div>

</body>
</html>

