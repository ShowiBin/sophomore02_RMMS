package controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import pojo.fgd;
import pojo.rxd;
import service.fgd_service;
import service.rxd_service;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@Controller
public class rxd_controller {
    @Autowired
    @Qualifier("rxd_service_impl")
    private rxd_service rxd_s;

    //查询全部的车行道,并且返回到一个展示页面
    @RequestMapping("/rxd")
    public String list(Model model){

        List<rxd> list = rxd_s.find_all_rxd();
        model.addAttribute("list",list);
        System.out.println(list.get(0));
        return "rxd";
    }

    @RequestMapping("/toaddrxd")
    public String to_add_rxd(){
        return "addrxd";
    }

    @RequestMapping("/addrxd")
    public String add_rxd(rxd r){

        System.out.println(r);
        rxd_s.add_rxd(r);
        return "redirect:/rxd";
    }

    @RequestMapping("/todeleterxd")
    public String to_delete_rxd(){ return "deleterxd";}

    @RequestMapping("deleterxd")
    public String delete_rxd(String road_id,String rxd_zyc){
        System.out.println(road_id+rxd_zyc);
        Map<String,Object> map =new HashMap<String, Object>();
        map.put("road_id",road_id);
        map.put("rxd_zyc",rxd_zyc);
        rxd_s.delete_rxd_part_para(map);
        return "redirect:/rxd";
    }

    @RequestMapping("toupdaterxd")
    public String to_update_rxd(String id,String rxd_zyc,Model model){
        Map<String,Object> map = new HashMap<String, Object>();
        map.put("road_id",id);
        map.put("rxd_zyc",rxd_zyc);
        System.out.println(id+rxd_zyc);
        rxd r = rxd_s.find_rxd_by_part_para(map);
        model.addAttribute("q_rxd",r);
        System.out.println(r);
        return "updaterxd";
    }

    @RequestMapping("updaterxd")
    public String update_fgd(rxd r){
        System.out.println(r);
        rxd_s.update_rxd(r);
        return "redirect:/rxd";
    }

    @RequestMapping("/queryrxd")
    public String query_road(String query_road_id,Model model){
        if(query_road_id == ""){
            System.out.println(query_road_id);
            List<rxd> list = rxd_s.find_all_rxd();
            model.addAttribute("list",list);
            return "rxd";
        }else{
            List<rxd> list = rxd_s.find_rxd_by_id(query_road_id);
            model.addAttribute("list",list);
            return "rxd";
        }
    }

}
