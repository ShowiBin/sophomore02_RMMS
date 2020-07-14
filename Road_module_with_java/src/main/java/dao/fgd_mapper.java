package dao;

import pojo.cxd;
import pojo.fgd;

import java.util.List;
import java.util.Map;

public interface fgd_mapper {
    //增
    int add_fgd(fgd ffgd);
    // 删
    int delete_fgd(String road_id,String fgd_zzyc);
    int delete_fgd_part_para(Map<String, Object> map);
    // 改
    int update_fgd(fgd ffgd);
    // 查
    List<fgd> find_all_fgd();
    List<fgd> find_fgd_by_id(String road_id);
    fgd find_fgd_by_part_para(Map<String, Object> map);

}
