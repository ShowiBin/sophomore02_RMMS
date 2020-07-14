package dao;

import pojo.cxd;
import pojo.fsss;
import pojo.road;

import java.util.List;

public interface road_mapper {
    //增
    int add_road(road ro);
    // 删
    int delete_road(String road_id);
    // 改
    int update_road(road ro);
    // 查
    List<road> find_all_road();
    List<road> find_road_by_id(String road_id);

    List<road> find_by_name(String road_name); // 2
    List<road> find_by_zx(String road_zx);  // 3
    List<road> find_by_qd(String road_qd);  // 4
    List<road> find_by_zd(String road_zd);  // 5
    List<road> find_by_sjdw(String road_sjdw);  // 6
    List<road> find_by_sgdw(String road_sgdw);  // 7
    List<road> find_by_dldj(String road_dldj);  // 8
    List<road> find_by_lmdj(String road_lmdj);  // 9
    List<road> find_by_sjss(String road_sjss);  // 10
    List<road> find_by_lfkdfw(String road_lfkdfw);  // 11
    List<road> find_by_dlcd(String road_dlcd);  // 12
    List<road> find_by_dlmj(String road_dlmj);  // 13
    List<road> find_by_AADT(String road_AADT);  // 14
    List<road> find_by_jtldj(String road_jtldj);  // 15
    List<road> find_by_ssxz(String road_ssxz);  // 16
    List<road> find_by_glfl(String road_glfl);  // 17
    List<road> find_by_gldw(String road_gldw);  // 18
    List<road> find_by_yhdw(String road_yhdw);  // 19
    List<road> find_by_jzny(String road_jzny);  // 20
}
