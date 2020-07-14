import org.junit.Test;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;
import pojo.cxd;
import service.cxd_service;

public class MyTest {
    @Test
    public void test(){
        ApplicationContext context = new ClassPathXmlApplicationContext("applicationContest.xml");
        cxd_service cxd_service_impl = (cxd_service)context.getBean("cxd_service_impl");
        for (cxd c : cxd_service_impl.find_all_cxd()) {
            System.out.println(c);
        }
    }
}
