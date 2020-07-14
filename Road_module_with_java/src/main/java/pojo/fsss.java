package pojo;

public class fsss {
    String road_id;
    Integer fsss_jcjsl;
    Integer fsss_ysksl;
    Integer fsss_lmpsl;
    Integer fsss_bzpsl;
    Float fsss_scmj;
    String fsss_qt;

    @Override
    public String toString() {
        return "fsss{" +
                "road_id='" + road_id + '\'' +
                ", fsss_jcjsl=" + fsss_jcjsl +
                ", fsss_ysksl=" + fsss_ysksl +
                ", fsss_lmpsl=" + fsss_lmpsl +
                ", fsss_bzpsl=" + fsss_bzpsl +
                ", fsss_scmj=" + fsss_scmj +
                ", fsss_qt='" + fsss_qt + '\'' +
                '}';
    }

    public String getRoad_id() {
        return road_id;
    }

    public void setRoad_id(String road_id) {
        this.road_id = road_id;
    }

    public Integer getFsss_jcjsl() {
        return fsss_jcjsl;
    }

    public void setFsss_jcjsl(Integer fsss_jcjsl) {
        this.fsss_jcjsl = fsss_jcjsl;
    }

    public Integer getFsss_ysksl() {
        return fsss_ysksl;
    }

    public void setFsss_ysksl(Integer fsss_ysksl) {
        this.fsss_ysksl = fsss_ysksl;
    }

    public Integer getFsss_lmpsl() {
        return fsss_lmpsl;
    }

    public void setFsss_lmpsl(Integer fsss_lmpsl) {
        this.fsss_lmpsl = fsss_lmpsl;
    }

    public Integer getFsss_bzpsl() {
        return fsss_bzpsl;
    }

    public void setFsss_bzpsl(Integer fsss_bzpsl) {
        this.fsss_bzpsl = fsss_bzpsl;
    }

    public Float getFsss_scmj() {
        return fsss_scmj;
    }

    public void setFsss_scmj(Float fsss_scmj) {
        this.fsss_scmj = fsss_scmj;
    }

    public String getFsss_qt() {
        return fsss_qt;
    }

    public void setFsss_qt(String fsss_qt) {
        this.fsss_qt = fsss_qt;
    }
}
