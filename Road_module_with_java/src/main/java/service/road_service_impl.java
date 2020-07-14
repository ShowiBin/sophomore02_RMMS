package service;

import dao.road_mapper;
import pojo.road;

import java.util.List;

public class road_service_impl implements road_service{
    private road_mapper road_m;

    public void setRoad_m(road_mapper road_m) {
        this.road_m = road_m;
    }

    public int add_road(road ro) {
        return road_m.add_road(ro);
    }

    public int delete_road(String road_id) {
        return road_m.delete_road(road_id);
    }

    public int update_road(road ro) {
        return road_m.update_road(ro);
    }

    public List<road> find_all_road() {
        return road_m.find_all_road();
    }

    public List<road> find_road_by_id(String road_id) {
        return road_m.find_road_by_id(road_id);
    }

    public List<road> find_by_name(String road_name) {
        return road_m.find_by_name(road_name);
    }

    public List<road> find_by_zx(String road_zx) {
        return road_m.find_by_zx(road_zx);
    }

    public List<road> find_by_qd(String road_qd) {
        return road_m.find_by_qd(road_qd);
    }

    public List<road> find_by_zd(String road_zd) {
        return road_m.find_by_zd(road_zd);
    }

    public List<road> find_by_sjdw(String road_sjdw) {
        return road_m.find_by_sjdw(road_sjdw);
    }

    public List<road> find_by_sgdw(String road_sgdw) {
        return road_m.find_by_sgdw(road_sgdw);
    }

    public List<road> find_by_dldj(String road_dldj) {
        return road_m.find_by_dldj(road_dldj);
    }

    public List<road> find_by_lmdj(String road_lmdj) {
        return road_m.find_by_lmdj(road_lmdj);
    }

    public List<road> find_by_sjss(String road_sjss) {
        return road_m.find_by_sjss(road_sjss);
    }

    public List<road> find_by_lfkdfw(String road_lfkdfw) {
        return road_m.find_by_lfkdfw(road_lfkdfw);
    }

    public List<road> find_by_dlcd(String road_dlcd) {
        return road_m.find_by_dlcd(road_dlcd);
    }

    public List<road> find_by_dlmj(String road_dlmj) {
        return road_m.find_by_dlmj(road_dlmj);
    }

    public List<road> find_by_AADT(String road_AADT) {
        return road_m.find_by_AADT(road_AADT);
    }

    public List<road> find_by_jtldj(String road_jtldj) {
        return road_m.find_by_jtldj(road_jtldj);
    }

    public List<road> find_by_ssxz(String road_ssxz) {
        return road_m.find_by_ssxz(road_ssxz);
    }

    public List<road> find_by_glfl(String road_glfl) {
        return road_m.find_by_glfl(road_glfl);
    }

    public List<road> find_by_gldw(String road_gldw) {
        return road_m.find_by_glfl(road_gldw);
    }

    public List<road> find_by_yhdw(String road_yhdw) {
        return road_m.find_by_yhdw(road_yhdw);
    }

    public List<road> find_by_jzny(String road_jzny) {
        return road_m.find_by_jzny(road_jzny);
    }
}
