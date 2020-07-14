package controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import pojo.cxd;
import service.cxd_service;

import java.util.ArrayList;
import java.util.List;

@Controller
public class cxd_controller {
    @Autowired
    @Qualifier("cxd_service_impl")
    private cxd_service cxd_s;

    //查询全部的车行道,并且返回到一个展示页面
    @RequestMapping("/cxd")
    public String list(Model model){
        List<cxd> list = cxd_s.find_all_cxd();

        model.addAttribute("list",list);
        return "cxd";
    }

    @RequestMapping("/toaddcxd")
    public String to_add_cxd(){
        return "addcxd";
    }

    @RequestMapping("addcxd")
    public String add_cxd(cxd c){
        System.out.println(c);
        cxd_s.add_cxd(c);
        return "redirect:/cxd";
    }

    @RequestMapping("/todeletecxd")
    public String to_delete_cxd(){
        return "deletecxd";
    }

    @RequestMapping("/deletecxd")
    public String delete_cxd(String road_id){
        System.out.println(road_id);
        cxd_s.delete_cxd(road_id);
        return "redirect:/cxd";
    }

    @RequestMapping("/toupdatecxd")
    public String to_update_cxd(String id,Model model){
        cxd c = cxd_s.find_cxd_by_id(id);
        System.out.println(id);
        model.addAttribute("q_cxd",c);
        return "updatecxd";
    }

    @RequestMapping("/updatecxd")
    public String update_cxd(cxd c){
        System.out.println(c);
        cxd_s.update_cxd(c);
        return "redirect:/cxd";
    }

    @RequestMapping("/querycxd")
    public String query_road(String query_road_id,Model model){
        if(query_road_id == ""){
            System.out.println(query_road_id);
            List<cxd> list = cxd_s.find_all_cxd();
            model.addAttribute("list",list);
            return "cxd";
        }else{
            cxd c = cxd_s.find_cxd_by_id(query_road_id);
            List<cxd> list = new ArrayList<cxd>();
            list.add(c);
            model.addAttribute("list",list);
            return "cxd";
        }
    }
}
