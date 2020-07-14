package controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import pojo.cxd;
import pojo.fsss;
import service.fsss_service;

import java.util.ArrayList;
import java.util.List;

@Controller
public class fsss_controller {
    @Autowired
    @Qualifier("fsss_service_impl")
    private fsss_service fsss_s;

    //查询全部的车行道,并且返回到一个展示页面
    @RequestMapping("/fsss")
    public String list(Model model){
        List<fsss> list = fsss_s.find_all_fsss();

        model.addAttribute("list",list);
        return "fsss";
    }

    @RequestMapping("/toaddfsss")
    public String to_add_fsss(){
        return "addfsss";
    }

    @RequestMapping("addfsss")
    public String add_fsss(fsss f){
        System.out.println(f);
        fsss_s.add_fsss(f);
        return "redirect:/fsss";
    }

    @RequestMapping("/todeletefsss")
    public String to_delete_fsss(){
        return "deletefsss";
    }

    @RequestMapping("/deletefsss")
    public String delete_fsss(String road_id){
        System.out.println(road_id);
        fsss_s.delete_fsss(road_id);
        return "redirect:/fsss";
    }

    @RequestMapping("/toupdatefsss")
    public String to_update_fsss(String id,Model model){
        fsss f = fsss_s.find_fsss_by_id(id);
        System.out.println(id);
        model.addAttribute("q_fsss",f);
        return "updatefsss";
    }

    @RequestMapping("/updatefsss")
    public String update_fsss(fsss f){
        System.out.println(f);
        fsss_s.update_fsss(f);
        return "redirect:/fsss";
    }

    @RequestMapping("/queryfsss")
    public String query_road(String query_road_id,Model model){
        if(query_road_id == ""){
            System.out.println(query_road_id);
            List<fsss> list = fsss_s.find_all_fsss();
            model.addAttribute("list",list);
            return "fsss";
        }else{
            fsss f = fsss_s.find_fsss_by_id(query_road_id);
            List<fsss> list = new ArrayList<fsss>();
            list.add(f);
            model.addAttribute("list",list);
            return "fsss";
        }
    }
}
