<%--
  Created by IntelliJ IDEA.
  User: hp
  Date: 2020/7/5
  Time: 18:38
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
                <h2><small>修改附属设施</small></h2>
            </div>
        </div>
    </div>

    <form action="${pageContext.request.contextPath}/updatefsss" method="post">
        <div class="form-group">
            <label>1.道路编号</label>
            <input type="text" name="road_id" class="form-control" value="${q_fsss.road_id}" required>
        </div>
        <div class="form-group">
            <label>2.检查井数量</label>
            <input type="text" name="fsss_jcjsl" class="form-control" value="${q_fsss.fsss_jcjsl}" required>
        </div>
        <div class="form-group">
            <label>3.雨水口数量</label>
            <input type="text" name="fsss_ysksl" class="form-control" value="${q_fsss.fsss_ysksl}" required>
        </div>
        <div class="form-group">
            <label>4.路名牌数量</label>
            <input type="text" name="fsss_lmpsl" class="form-control" value="${q_fsss.fsss_lmpsl}" required>
        </div>
        <div class="form-group">
            <label>5.标志牌数量</label>
            <input type="text" name="fsss_bzpsl" class="form-control" value="${q_fsss.fsss_bzpsl}" required>
        </div>
        <div class="form-group">
            <label>6.树池面积</label>
            <input type="text" name="fsss_scmj" class="form-control" value="${q_fsss.fsss_scmj}" required>
        </div>
        <div class="form-group">
            <label>7.其他</label>
            <input type="text" name="fsss_qt" class="form-control" value="${q_fsss.fsss_qt}" required>
        </div>
        <div class="form-group">
            <input type="submit" class="form-control" value="修改">
        </div>

    </form>

</div>

</body>
</html>