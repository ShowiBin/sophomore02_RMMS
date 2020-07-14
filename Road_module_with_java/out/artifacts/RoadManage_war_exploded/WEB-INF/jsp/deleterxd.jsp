<%--
  Created by IntelliJ IDEA.
  User: hp
  Date: 2020/7/6
  Time: 12:59
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
                <h2><small>删除人行道信息</small></h2>
            </div>
        </div>
    </div>

    <form action="${pageContext.request.contextPath}/deleterxd" method="post">
        <div class="form-group">
            <label>请输入需要删除人行道的道路编号</label>
            <input type="text" name="road_id" class="form-control" required>
        </div>
        <div class="form-group">
            <label>请输入需要删除的人行道属于哪一侧</label>
            <input type="text" name="rxd_zyc" class="form-control" required>
        </div>
        <div class="form-group">
            <input type="submit" class="form-control" value="一键删除">
        </div>
    </form>

</div>
</body>
</html>
