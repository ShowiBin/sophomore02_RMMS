package dao;

import pojo.cxd;

import java.util.List;

public interface cxd_mapper {
    //增
    int add_cxd(cxd ccxd);
    // 删
    int delete_cxd(String road_id);
    // 改
    int update_cxd(cxd ccxd);
    // 查
    List<cxd> find_all_cxd();
    cxd find_cxd_by_id(String road_id);



}
