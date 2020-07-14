<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%--
  Created by IntelliJ IDEA.
  User: hp
  Date: 2020/7/5
  Time: 19:06
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>道路资料展示</title>
    <link href="https://cdn.staticfile.org/twitter-bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet">

</head>

<body>
<div class="container">
    <div class="row clearfix">
        <div class="col-md-12 column">
            <div class="page-header">
                <h2><small>道路详细信息</small></h2>
            </div>
        </div>

        <div class="row">
            <div class="col-md-1 column">
                <a class="btn btn-primary" href="${pageContext.request.contextPath}/toaddroad">新增道路</a>
            </div>


            <div class="col-md-1 column">
                <a class="btn btn-primary" href="${pageContext.request.contextPath}/todeleteroad">删除已有道路</a>
            </div>


            <div class="col-md-10 column">
                <form class="form-inline" action="${pageContext.request.contextPath}/queryroad" method="post" style="float: right">
                    <select class="form-control" name="property"  >
                        <option value="0">按照属性搜索</option>
                        <option value="1">道路编号</option>
                        <option value="2">道路名称</option>
                        <option value="3">道路走向</option>
                        <option value="4">起点</option>
                        <option value="5">终点</option>
                        <option value="6">设计单位</option>
                        <option value="7">施工单位</option>
                        <option value="8">道路等级</option>
                        <option value="9">路面等级</option>
                        <option value="10">设计时速</option>
                        <option value="11">路幅宽度范围</option>
                        <option value="12">道路长度</option>
                        <option value="13">道路面积</option>
                        <option value="14">AADT</option>
                        <option value="15">交通量等级</option>
                        <option value="16">所属乡镇</option>
                        <option value="17">管理分类</option>
                        <option value="18">管理单位</option>
                        <option value="19">养护年月</option>
                        <option value="20">建造年月</option>

                    </select>
                    <input type="text" name="query_road" class="form-control" placeholder="请输入要搜索内容">
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
                    <th>道路名称</th>
                    <th>道路走向</th>
                    <th>起点</th>
                    <th>终点</th>
                    <th>设计单位</th>
                    <th>施工单位</th>
                    <th>道路等级</th>
                    <th>路面等级</th>
                    <th>设计时速</th>
                    <th>路幅宽度范围</th>
                    <th>道路长度</th>
                    <th>道路面积</th>
                    <th>AADT</th>
                    <th>交通量等级</th>
                    <th>所属乡镇</th>
                    <th>管理分类</th>
                    <th>管理单位</th>
                    <th>养护单位</th>
                    <th>建造年月</th>
                </tr>
                </thead>
                <tbody>

                <c:forEach var="c" items="${list}">
                    <tr>
                        <td>${c.road_id}</td>
                        <td>${c.road_name}</td>
                        <td>${c.road_zx}</td>
                        <td>${c.road_qd}</td>
                        <td>${c.road_zd}</td>
                        <td>${c.road_sjdw}</td>
                        <td>${c.road_sgdw}</td>
                        <td>${c.road_dldj}</td>
                        <td>${c.road_lmdj}</td>
                        <td>${c.road_sjss}</td>
                        <td>${c.road_lfkdfw}</td>
                        <td>${c.road_dlcd}</td>
                        <td>${c.road_dlmj}</td>
                        <td>${c.road_AADT}</td>
                        <td>${c.road_jtldj}</td>
                        <td>${c.road_ssxz}</td>
                        <td>${c.road_glfl}</td>
                        <td>${c.road_gldw}</td>
                        <td>${c.road_yhdw}</td>
                        <td>${c.road_jzny}</td>
                        <td>
                            <a href="${pageContext.request.contextPath}/toupdateroad?id=${c.road_id}">修改</a>
                        </td>
                        <td>
                            <a href="https://map.baidu.com/search/${c.road_name}/@11833432.435328947,3407250.6950000003,14.75z?querytype=s&da_src=shareurl&wd=${c.road_name}&c=132&src=0&pn=0&sug=0&l=9&b=(11668624.680566039,3263656.7922641505;12128792.858463611,3492256.4677358484)&from=webmap&biz_forward=%7B">查看</a>
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