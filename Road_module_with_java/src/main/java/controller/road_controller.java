package controller;


import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import pojo.cxd;
import pojo.road;
import pojo.v_road;
import service.road_service;

import java.text.DateFormat;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;

@Controller
public class road_controller {

    @Autowired
    @Qualifier("road_service_impl")
    private road_service road_s;

    //查询全部的车行道,并且返回到一个展示页面
    @RequestMapping("/road")
    public String list(Model model){
        List<road> list = road_s.find_all_road();

        model.addAttribute("list",list);
        return "road";
    }

    @RequestMapping("/toaddroad")
    public String to_add_road(){
        return "addroad";
    }

    @RequestMapping("addroad")
    public String add_road(road r) {
        System.out.println(r);
        road_s.add_road(r);
        return "redirect:/road";

    }

    @RequestMapping("/todeleteroad")
    public String to_delete_road(){
        return "deleteroad";
    }

    @RequestMapping("/deleteroad")
    public String delete_road(String road_id){
        System.out.println(road_id);
        road_s.delete_road(road_id);
        return "redirect:/road";
    }

    @RequestMapping("/toupdateroad")
    public String to_update_road(String id,Model model){
        List<road> list = road_s.find_road_by_id(id);
        System.out.println(id);
        model.addAttribute("q_road",list.get(0));
        return "updateroad";
    }

    @RequestMapping("/updateroad")
    public String update_road(road r){
        System.out.println(r);
        road_s.update_road(r);
        return "redirect:/road";
    }

    @RequestMapping("/queryroad")
    public String query_road(String query_road,String property,Model model) {
        System.out.println(property + "  " + query_road);
        if (query_road == "") {
            System.out.println(query_road);
            List<road> list = road_s.find_all_road();
            model.addAttribute("list", list);
            return "road";
        } else {
            if (property.equals("0")) {
                List<road> list = road_s.find_road_by_id(query_road);
                model.addAttribute("list", list);


            } else if (property.equals("1")) {
                List<road> list = road_s.find_road_by_id(query_road);
                model.addAttribute("list", list);


            } else if (property.equals("2")) {
                List<road> list = road_s.find_by_name(query_road);
                model.addAttribute("list", list);



            } else if (property.equals("3")) {
                List<road> list = road_s.find_by_zx(query_road);
                model.addAttribute("list", list);


            } else if (property.equals("4")) {
                List<road> list = road_s.find_by_qd(query_road);
                model.addAttribute("list", list);


            }else if (property.equals("5")) {
            List<road> list = road_s.find_by_zd(query_road);
            model.addAttribute("list", list);


            }  else if (property.equals("6")) {
                List<road> list = road_s.find_by_sjdw(query_road);
                model.addAttribute("list", list);


            } else if (property.equals("7")) {
                List<road> list = road_s.find_by_sgdw(query_road);
                model.addAttribute("list", list);

            } else if (property.equals("8")) {
                List<road> list = road_s.find_by_dldj(query_road);
                model.addAttribute("list", list);


            } else if (property.equals("9")) {
                List<road> list = road_s.find_by_lmdj(query_road);
                model.addAttribute("list", list);


            } else if (property.equals("10")) {
                List<road> list = road_s.find_by_sjss(query_road);
                model.addAttribute("list", list);


            } else if (property.equals("11")) {
                List<road> list = road_s.find_by_lfkdfw(query_road);
                model.addAttribute("list", list);


            } else if (property.equals("12")) {
                List<road> list = road_s.find_by_dlcd(query_road);
                model.addAttribute("list", list);


            } else if (property.equals("13")) {
                List<road> list = road_s.find_by_dlmj(query_road);
                model.addAttribute("list", list);


            } else if (property.equals("14")) {
                List<road> list = road_s.find_by_AADT(query_road);
                model.addAttribute("list", list);


            } else if (property.equals("15")) {
                List<road> list = road_s.find_by_jtldj(query_road);
                model.addAttribute("list", list);


            } else if (property.equals("16")) {
                List<road> list = road_s.find_by_ssxz(query_road);
                model.addAttribute("list", list);


            } else if (property.equals("17")) {
                List<road> list = road_s.find_by_glfl(query_road);
                model.addAttribute("list", list);


            } else if (property.equals("18")) {
                List<road> list = road_s.find_by_gldw(query_road);
                model.addAttribute("list", list);


            } else if (property.equals("19")) {
                List<road> list = road_s.find_by_yhdw(query_road);
                model.addAttribute("list", list);


            } else if (property.equals("20")) {
                List<road> list = road_s.find_by_jzny(query_road);
                model.addAttribute("list", list);

            }
            return "road";

        }
    }

}
