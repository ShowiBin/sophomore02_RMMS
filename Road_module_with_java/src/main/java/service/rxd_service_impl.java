package service;

import dao.rxd_mapper;
import pojo.rxd;

import java.util.List;
import java.util.Map;

public class rxd_service_impl implements rxd_service{

    private rxd_mapper rxd_m;

    public void setRxd_m(rxd_mapper rxd_m) {
        this.rxd_m = rxd_m;
    }

    public int add_rxd(rxd rrxd) {
        return rxd_m.add_rxd(rrxd);
    }

//    public int delete_rxd(String road_id, String rxd_zyc) {
//        return rxd_m.delete_rxd(road_id,rxd_zyc);
//    }

    public int delete_rxd_part_para(Map<String, Object> map) {
        return rxd_m.delete_rxd_part_para(map);
    }

    public int update_rxd(rxd rrxd) {
        return rxd_m.update_rxd(rrxd);
    }

    public List<rxd> find_all_rxd() {
        return rxd_m.find_all_rxd();
    }

    public List<rxd> find_rxd_by_id(String road_id) {
        return rxd_m.find_rxd_by_id(road_id);
    }

    public rxd find_rxd_by_part_para(Map<String, Object> map) {
        return rxd_m.find_rxd_by_part_para(map);
    }
}
