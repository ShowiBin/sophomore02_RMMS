package service;

import dao.fgd_mapper;
import pojo.fgd;

import java.util.List;
import java.util.Map;

public class fgd_service_impl implements fgd_service{
    private fgd_mapper fgd_m;

    public void setFgd_m(fgd_mapper fgd_m) {
        this.fgd_m = fgd_m;
    }

    public int add_fgd(fgd ffgd) {
        return fgd_m.add_fgd(ffgd);
    }

    public int delete_fgd(String road_id,String fgd_zzyc) {
        return fgd_m.delete_fgd(road_id,fgd_zzyc);
    }

    public int delete_fgd_part_para(Map<String, Object> map) {
        return fgd_m.delete_fgd_part_para(map);
    }


    public int update_fgd(fgd ffgd) {
        return fgd_m.update_fgd(ffgd);
    }

    public List<fgd> find_all_fgd() {
        return fgd_m.find_all_fgd();
    }

    public List<fgd> find_fgd_by_id(String road_id) {
        return fgd_m.find_fgd_by_id(road_id);
    }

    public fgd find_fgd_by_part_para(Map<String, Object> map) {
        return fgd_m.find_fgd_by_part_para(map);
    }
}
