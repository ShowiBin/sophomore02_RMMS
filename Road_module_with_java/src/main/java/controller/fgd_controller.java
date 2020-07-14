package controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import pojo.cxd;
import pojo.fgd;
import service.fgd_service;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@Controller
public class fgd_controller {
    @Autowired
    @Qualifier("fgd_service_impl")
    private fgd_service fgd_s;

    //查询全部的车行道,并且返回到一个展示页面
    @RequestMapping("/fgd")
    public String list(Model model){
        List<fgd> list = fgd_s.find_all_fgd();
        model.addAttribute("list",list);
        return "fgd";
    }

    @RequestMapping("/toaddfgd")
    public String to_add_fgd(){
        return "addfgd";
    }

    @RequestMapping("/addfgd")
    public String add_fgd(fgd f){
        System.out.println(f);
        fgd_s.add_fgd(f);
        return "redirect:/fgd";
    }

    @RequestMapping("/todeletefgd")
    public String to_delete_fgd(){ return "deletefgd";}

    @RequestMapping("deletefgd")
    public String delete_fgd(String road_id,String fgd_zzyc){
        System.out.println(road_id+fgd_zzyc);
        Map<String,Object> map =new HashMap<String, Object>();
        map.put("road_id",road_id);
        map.put("fgd_zzyc",fgd_zzyc);
        fgd_s.delete_fgd_part_para(map);
        return "redirect:/fgd";
    }

    @RequestMapping("toupdatefgd")
    public String to_update_fgd(String id,String zzyc,Model model){
        Map<String,Object> map = new HashMap<String, Object>();
        map.put("road_id",id);
        map.put("fgd_zzyc",zzyc);
        System.out.println(id+zzyc);
        fgd f = fgd_s.find_fgd_by_part_para(map);
        model.addAttribute("q_fgd",f);
        System.out.println(f);
        return "updatefgd";
    }

    @RequestMapping("updatefgd")
    public String update_fgd(fgd f){
        System.out.println(f);
        fgd_s.update_fgd(f);
        return "redirect:/fgd";
    }

    @RequestMapping("/queryfgd")
    public String query_road(String query_road_id,Model model){
        if(query_road_id == ""){
            System.out.println(query_road_id);
            List<fgd> list = fgd_s.find_all_fgd();
            model.addAttribute("list",list);
            return "fgd";
        }else{
            List<fgd> list = fgd_s.find_fgd_by_id(query_road_id);
            model.addAttribute("list",list);
            return "fgd";
        }
    }

}
