package dao;

import pojo.cxd;
import pojo.fsss;

import java.util.List;

public interface fsss_mapper {
    //增
    int add_fsss(fsss fs);
    // 删
    int delete_fsss(String road_id);
    // 改
    int update_fsss(fsss fs);
    // 查
    List<fsss> find_all_fsss();
    fsss find_fsss_by_id(String road_id);
}
