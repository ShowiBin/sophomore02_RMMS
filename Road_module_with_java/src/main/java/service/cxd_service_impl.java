package service;

import dao.cxd_mapper;
import pojo.cxd;

import java.util.List;

public class cxd_service_impl implements cxd_service{

    private cxd_mapper cxd_m;

    public void setCxd_m(cxd_mapper cxd_m) {
        this.cxd_m = cxd_m;
    }

    public int add_cxd(cxd ccxd) {
        return cxd_m.add_cxd(ccxd);
    }

    public int delete_cxd(String road_id) {
        return cxd_m.delete_cxd(road_id);
    }

    public int update_cxd(cxd ccxd) {
        return cxd_m.update_cxd(ccxd);
    }

    public List<cxd> find_all_cxd() {
        return cxd_m.find_all_cxd();
    }

    public cxd find_cxd_by_id(String road_id) {
        return cxd_m.find_cxd_by_id(road_id);
    }
}
