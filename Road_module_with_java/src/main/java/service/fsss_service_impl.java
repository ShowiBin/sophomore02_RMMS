package service;

import dao.fsss_mapper;
import pojo.fsss;

import java.util.List;

public class fsss_service_impl implements fsss_service{
    private fsss_mapper fsss_m;

    public void setFsss_m(fsss_mapper fsss_m) {
        this.fsss_m = fsss_m;
    }

    public int add_fsss(fsss fs) {
        return fsss_m.add_fsss(fs);
    }

    public int delete_fsss(String road_id) {
        return fsss_m.delete_fsss(road_id);
    }

    public int update_fsss(fsss fs) {
        return fsss_m.update_fsss(fs);
    }

    public List<fsss> find_all_fsss() {
        return fsss_m.find_all_fsss();
    }

    public fsss find_fsss_by_id(String road_id) {
        return fsss_m.find_fsss_by_id(road_id);
    }
}
