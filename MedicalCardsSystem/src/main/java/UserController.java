import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
public class UserController {
    @GetMapping("/")
    public String main(
            @RequestParam(name="name", required = false, defaultValue="world") String name, Model model) {
        model.addAttribute("name", name);
        return "index/reg";
    }

}
