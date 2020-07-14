package dao;

import pojo.fgd;
import pojo.road;
import pojo.rxd;

import java.util.List;
import java.util.Map;

public interface rxd_mapper {
    //增
    int add_rxd(rxd rrxd);
    // 删
    int delete_rxd(String road_id,String rxd_zyc);
    int delete_rxd_part_para(Map<String, Object> map);
    // 改
    int update_rxd(rxd rrxd);
    // 查
    List<rxd> find_all_rxd();
    List<rxd> find_rxd_by_id(String road_id);
    rxd find_rxd_by_part_para(Map<String, Object> map);
}
